from django.conf.urls import patterns, url


urlpatterns = patterns('backend.views',
    url(r'^$', 'landing_page'),
)