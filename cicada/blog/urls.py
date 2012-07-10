from django.conf.urls import patterns, url

urlpatterns = patterns('cicada.blog.views',
    url(r'^$', 'index'),
    url(r'^(?P<post_id>\d+)/$', 'read'),
)