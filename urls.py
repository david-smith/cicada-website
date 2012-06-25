from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cicada.views.home', name='home'),
    # url(r'^cicada/', include('cicada.foo.urls')),
    
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    
)
