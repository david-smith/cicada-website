from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),
    url(r'^(?P<post_id>\d+)/$', 'read'),
)