from django.db import models

# Create your models here.

class MoviePlatform(models.Model):
    ott_name = models.CharField(max_length=250)
    cost = models.PositiveIntegerField()
    
    def __str__(self):
        return self.ott_name

class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    active = models.BooleanField()
    ott= models.ForeignKey(MoviePlatform,on_delete=models.CASCADE,related_name="ott")
    
    def __str__(self):
        return self.name
    

    
    