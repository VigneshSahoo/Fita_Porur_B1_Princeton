from django.db import models
from django.forms import ModelForm


class Rooms(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=250, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    course_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.first_name


class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['first_name',
                  'last_name',
                  'course_name'
                  ]