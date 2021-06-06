from .models import Users
from rest_framework.response import Response
from rest_framework import status
class User:
    def __init__(self):
        pass

    def create_user(self,request):
        email= request.data.get('email')
        if email != None and User.validateEmail(email):
            user = Users.objects.filter(email=email)
            print
            if not user:
                return [True,"create user"]
            else:
                return [False,"Duplicate email "]
        else:
            return [False,"inalid email input "]
    @staticmethod
    def validateEmail(email):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False










