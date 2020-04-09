from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Grade(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)

class Assignment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='assigns')
    title = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='assigns')
    filename = models.CharField(max_length=255)
    duedate   = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return  self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    assignments = models.ManyToManyField(Assignment)
    interests = models.ManyToManyField(Grade, related_name='interested_students')

    def __str__(self):
        return self.user.username

