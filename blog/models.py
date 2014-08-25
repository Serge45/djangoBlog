from django.db import models
from django.contrib.auth.models import User
import datetime

class BlogPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    post_datetime = models.DateTimeField(auto_now_add=True, name='post date')
    last_update_datetime = models.DateTimeField(auto_now=True, name='last update date')

    def __unicode__(self):
        return '%s' %(self.title)
