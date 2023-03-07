from django.db import models

class Movie(models.Model):
    name = models.CharField()
    year = models.IntegerField(max_length=4)
    description = models.TextField()