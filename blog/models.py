from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class BlogPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    post_datetime = models.DateTimeField(auto_now_add=True)
    last_update_datetime = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=40, unique=True)
    site = models.ForeignKey(Site)

    class Meta:
        ordering = ["-post_datetime"]

    def get_absolute_url(self):
        return '/%s/%s/%s/' % (self.post_datetime.year, self.post_datetime.month, self.slug)

    def __unicode__(self):
        return '%s' %(self.title)
