"""
utility urls file
"""
# third party imports
from rest_framework import routers

# local imports
from .views import *


router = routers.SimpleRouter()

router.register('signup', SignupViewSet, 'signup')
router.register('login', LoginViewSet, 'login')
router.register('departments', DepartmentViewSet, 'department')
router.register('courses', CourseViewSet, 'course')
router.register('students', StudentViewSet, 'student')
router.register('attendance_logs', AttendanceLogViewSet, 'attendance')

urlpatterns = [

] + router.urls
