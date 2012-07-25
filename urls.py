from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from tastypie.api import Api
from api import UserResource, DeviceResource, SightingResource

admin.autodiscover()

#API
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(DeviceResource())
v1_api.register(SightingResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cicada.views.home', name='home'),
    # url(r'^cicada/', include('cicada.foo.urls')),
    
    
    url(r'^$', 'cicada.blog.views.main_page'),
    url(r'^about/team$', TemplateView.as_view(template_name='team.html')),
    url(r'^about/cicada$', TemplateView.as_view(template_name='cicada.html')),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html')),
    url(r'^app$', TemplateView.as_view(template_name='app.html')),
    url(r'^login$', 'cicada.core.views.login_view'),
    url(r'^logout$', 'cicada.core.views.logout_view'),
    url(r'^weather$', 'cicada.core.views.weather'),
    
    url(r'^tracker/', include('cicada.backend.urls')),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('cicada.blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    # API
    url(r'^api/', include(v1_api.urls)),
    
    # django-socialregistration
    url(r'^account/', include('social_auth.urls')),
    
)
