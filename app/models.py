from django.db import models

# Create your models here.

class Ipl(models.Model):
    Tname=models.CharField(max_length=100)
    Tcaptain=models.CharField(max_length=100)
    Nooftrophy=models.IntegerField()

    def __str__(self):
        return self.Tname