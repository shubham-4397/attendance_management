from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from .messages import UserType


class User(AbstractUser):
    """user model"""
    type = models.CharField(max_length=20, default=UserType.TEACHER.value)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Department(models.Model):
    """Model to handle department data"""
    department_name = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    """Course model"""
    course_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField()
    class_name = models.CharField(max_length=255)
    lecture_hours = models.IntegerField()
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    """student model"""
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=255)
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class AttendanceLog(models.Model):
    """attendance model"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    present = models.BooleanField()
    submitted_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
