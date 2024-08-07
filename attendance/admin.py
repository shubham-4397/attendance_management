from django.contrib import admin
from attendance.models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    admin interface for User.
    """
    list_display = ['id', 'email', 'username']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    admin interface for student.
    """
    list_display = ['id', 'full_name']


@admin.register(AttendanceLog)
class AttendanceAdmin(admin.ModelAdmin):
    """
    admin interface for User.
    """
    list_display = ['id', 'student', 'course']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    admin interface for course.
    """
    list_display = ['id', 'course_name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    admin interface for department.
    """
    list_display = ['id', 'department_name']
