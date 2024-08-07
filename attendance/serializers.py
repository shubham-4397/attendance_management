"""
User Serializer
"""
from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth import get_user_model

# local imports
from .messages import ERROR_MESSAGE
from .models import *

USER = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    """
    used to serialize the User objects
    """
    full_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        """
        meta class
        """
        model = USER
        fields = ('full_name', 'username', 'email', 'password')

    def validate(self, attrs):
        """ used to validate the data """
        qs = USER.objects.filter(Q(email=attrs['email']) | Q(username=attrs['username']))
        if qs:
            raise serializers.ValidationError(ERROR_MESSAGE['already-exist'])
        return attrs

    def create(self, validated_data):
        """used to create the user"""
        password = validated_data['password']
        user = USER.objects.create(**validated_data)
        user.set_password(password)
        user.save(update_fields=['password'])
        return user


class LoginSerializer(serializers.ModelSerializer):
    """
    used to serialize the User objects
    """

    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        """
        meta class
        """
        model = USER
        fields = ('email', 'password')

    def validate(self, attrs):
        """ used to validate the data """
        user = USER.objects.filter(email__iexact=attrs['email']).first()
        if not user:
            raise serializers.ValidationError(ERROR_MESSAGE['email-not-found'])
        elif user.is_active is False:
            raise serializers.ValidationError(ERROR_MESSAGE['user-deactivated'])
        elif not user.check_password(attrs['password']):
            raise serializers.ValidationError(ERROR_MESSAGE['incorrect-password'])
        self.context.update({'user': user})
        return attrs

    def create(self, validated_data):
        """used to create the user"""
        return self.context.get('user')


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Department serializer
    """
    class Meta:
        model = Department
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Course serializer
    """
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    """
    Student serializer
    """
    class Meta:
        model = Student
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    class Meta:
        model = User
        fields = '__all__'


class AttendanceLogSerializer(serializers.ModelSerializer):
    """
    Attendance serializer
    """

    class Meta:
        model = AttendanceLog
        fields = '__all__'
