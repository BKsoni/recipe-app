from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    views = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name
    
class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    student_id = models.OneToOneField(StudentID, on_delete=models.SET_NULL, null=True, blank=True)
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100, unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField(null=True, blank=True)
    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'