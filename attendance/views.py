from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# local imports
from .messages import SUCCESS_MESSAGE
from .serializers import *
from .models import *

USER = get_user_model()


class SignupViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    signup class viewset
    """
    serializer_class = SignupSerializer
    queryset = USER.objects.all()

    def create(self, request, *args, **kwargs):
        """used to create a user"""
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details': SUCCESS_MESSAGE['user-created']})


class LoginViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    Login class viewset
    """
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """used to log in the user"""
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh_token = RefreshToken.for_user(user)
        tokens = {'refresh_token': str(refresh_token),
                  'access_token': str(refresh_token.access_token)}
        return Response({'details': tokens})


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    used to perform operations on department model
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """
    used to perform operations on course model
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    """
    used to perform operations on student model
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class AttendanceLogViewSet(viewsets.ModelViewSet):
    """
    Used to perform operation on attendance
    """
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer
    permission_classes = [IsAuthenticated]
