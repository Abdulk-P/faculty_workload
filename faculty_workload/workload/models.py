from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other profile fields here

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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




