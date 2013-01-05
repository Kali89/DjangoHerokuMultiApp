from django.db import models

class User(models.Model):
    username = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=40)

    def __unicode__(self):
        return self.username

    class Meta:
        ordering = ('created',)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)
    
