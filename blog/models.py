from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class create_blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog_images\\")
    content = models.TextField()
    meta_description = models.TextField()
    date = models.DateTimeField(default = now)

class resources(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="resource_images\\")
    content = models.TextField()
    meta_description = models.TextField()
    date = models.DateTimeField(default = now)
    tag = models.CharField(max_length=50)