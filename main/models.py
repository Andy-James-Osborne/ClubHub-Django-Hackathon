from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.username

class Event(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    body = models.TextField()
    # image = models.ImageField('image')
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name