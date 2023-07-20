from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=250, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
