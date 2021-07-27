from django.db import models

# Create your models here.
class add_movie(models.Model):
    movie_name = models.CharField(max_length=150)
