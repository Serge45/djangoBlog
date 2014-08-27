from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import BlogPost
from blog import views

urlpatterns = patterns('',
                       #url(r'^$', views.index, name='index'),
                       url(r'^$', ListView.as_view(model=BlogPost)),
                       url(r'^(?P<post_id>\d+)/$', views.blog_content, name='content'),
)