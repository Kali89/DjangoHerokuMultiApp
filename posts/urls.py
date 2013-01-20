from django.conf.urls import patterns, url
from views import user_profile	

urlpatterns = patterns('posts.views',
    url(r'^$', 'index'),
    url(r'^(?P<username>)/$', user_profile),
)
