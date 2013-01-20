from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=100)

    def __unicode__(self):
        return self.title
