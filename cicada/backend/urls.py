from django.conf.urls import patterns, url


urlpatterns = patterns('cicada.backend.views',
    url(r'^$', 'landing_page'),
)