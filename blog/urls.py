from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import BlogPost
from blog import views

urlpatterns = patterns('',
                       #url(r'^$', ListView.as_view(model=BlogPost)),
                       url(r'^(?P<page>\d+)?/?', ListView.as_view(model=BlogPost, paginate_by=5, )),
)