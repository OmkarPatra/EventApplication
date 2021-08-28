from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.urls import reverse
from django.conf import settings

# Create your models here.

def get_like_url(self):
    return reverse("posts:like-toggle", kwargs={"slug": self.slug})

def get_api_like_url(self):
    return reverse("posts:like-api-toggle", kwargs={"slug": self.slug})

class EventList(models.Model):
    title = models.CharField(max_length=250,blank=False,null=False)
    host = models.ForeignKey(User, on_delete = models.CASCADE)
    image = ImageField()
    event_date = models.DateField(auto_now_add=False)
    event_time = models.TimeField(auto_now_add=False)
    location = models.CharField(max_length=255)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('home')
