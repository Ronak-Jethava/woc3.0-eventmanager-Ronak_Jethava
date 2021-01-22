from django.db import models
# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    location = models.CharField(max_length=120)
    poster = models.FileField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    last_date = models.DateField()
    last_time = models.TimeField()
    email = models.EmailField()
    pswd = models.CharField(max_length=20)

    def __str__(self):
        return self.name