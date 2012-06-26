from tastypie.resources import ModelResource
from tastypie import fields
from core.models import Device, Sighting
from django.contrib.auth.models import User
from tastypie.authentication import ApiKeyAuthentication

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
        allowed_methods = ['get']