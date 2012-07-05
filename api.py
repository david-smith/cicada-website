from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource
from tastypie import fields
from core.models import Device, Sighting
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from tastypie.authentication import ApiKeyAuthentication
from django.conf.urls.defaults import url

class DeviceApiKeyAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        uuid = request.GET.get('uuid') or request.POST.get('uuid')
        api_key = request.GET.get('api_key') or request.POST.get('api_key')

        if not uuid or not api_key:
            return self._unauthorized()

        try:
            device = Device.objects.get(uuid=uuid, api_key=api_key)
        except (Device.DoesNotExist, Device.MultipleObjectsReturned):
            return self._unauthorized()

        request.device = device
        return True
    
    def get_identifier(self, request):
        return request.REQUEST.get('uuid', 'nouser')

class UserResource(ModelResource):
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        fields = ['id', 'username', 'email', 'date_joined']
        allowed_methods = ['get']
        
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user = request.user)
    
    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('do_login'), name='api_login')
        ]
    
    def do_login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        username = request.POST['username']
        password = request.POST['password']
        uuid = request.POST['uuid']
        device_name = request.POST['name']
        device_type = request.POST['device_type']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    device = Device.objects.get(user = user, uuid = uuid)
                except Device.DoesNotExist:
                    import uuid, hmac
                    try:
                        from hashlib import sha1
                    except ImportError:
                        import sha
                        sha1 = sha.sha
                    new_uuid = uuid.uuid4()
                    device = Device()
                    device.user_id = user.id
                    device.uuid = uuid
                    device.api_key = hmac.new(str(new_uuid), digestmod=sha1).hexdigest()
                    device.name = device_name
                    device.device_type = device_type
                    device.save()
                return self.create_response(request, {'success' : True, 'api_key' : device.api_key})
            else:
                return self.create_response(request, {'success' : False, 'error' : 'User not active'})
        else:
            return self.create_response(request, {'success' : False, 'error' : 'Username and/or password incorrect'})
           
class DeviceResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        resource_name = 'device'
        queryset = Device.objects.all()
        allowed_methods = ['get']
        
class SightingResource(ModelResource):
    device = fields.ForeignKey(DeviceResource, 'device')
    class Meta:
        resource_name = 'sighting'
        queryset = Sighting.objects.all()
        allowed_methods = ['get', 'post']
        
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user = request.user)
