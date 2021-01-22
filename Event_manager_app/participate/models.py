from django.db import models

# Create your models here.

class Participate(models.Model):
    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=12)
    email = models.EmailField()
    event = models.CharField(max_length=120)
    no_of_people = models.IntegerField()

    def __str__(self):
        return self.name