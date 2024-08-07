"""
Messages File
"""
from enum import Enum


SUCCESS_MESSAGE = {
    'user-created': 'Signed up successfully',

}

ERROR_MESSAGE = {
    'email-not-found': 'User with this email does not exist',
    'user-deactivated': 'Account has been deactivated',
    'incorrect-password': 'Incorrect password',
    'already-exist': 'User with this email or username already exists.'
}


class UserType(Enum):
    """user type choices"""
    TEACHER = 'teacher'
    ADMIN = 'admin'
