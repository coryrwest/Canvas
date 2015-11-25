from django.db import models

# Create your models here.

class Album(models.Model):
  name = models.CharField(max_length=250)
  

class Photo(models.Model):
  file_name = models.CharField(max_length=500)
  name = models.CharField(max_length=500)
  tags = models.TextField()
  album = models.ManyToManyField(Album, related_name='photos', related_query_name='photo')