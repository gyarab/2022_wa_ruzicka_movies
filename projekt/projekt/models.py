from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.TextField()
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} ({self.year})'
    
class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"