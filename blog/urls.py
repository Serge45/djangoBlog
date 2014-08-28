from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import BlogPost

urlpatterns = patterns('',
                       #url(r'^$', ListView.as_view(model=BlogPost)),
                       url(r'^(?P<page>\d+)?/?$', ListView.as_view(model=BlogPost, paginate_by=5, )),
                       url(r'^(?P<post_datetime__year>\d{4})/(?P<post_datetime__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
                           DetailView.as_view(model=BlogPost)),
)