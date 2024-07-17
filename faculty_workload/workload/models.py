from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Workload(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    teaching_hours = models.IntegerField()
    research_hours = models.IntegerField()
    admin_hours = models.IntegerField()
    course = models.CharField(max_length=100, default='Django')

    def __str__(self):
        return f"{self.faculty.name} - Teaching: {self.teaching_hours}, Research: {self.research_hours}, Admin: {self.admin_hours}"

