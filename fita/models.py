from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    date = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name
