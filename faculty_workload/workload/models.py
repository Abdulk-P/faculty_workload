from django.db import models

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class Workload(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    hours = models.IntegerField()
