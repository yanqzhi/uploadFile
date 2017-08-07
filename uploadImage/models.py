from django.db import models


# Create your models here.

class ImageFile(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    thumbnail = models.CharField(max_length=100)
