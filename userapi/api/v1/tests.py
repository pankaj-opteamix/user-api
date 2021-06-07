from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Users
from .serializers import UsersSerializer

from rest_framework.test import APITestCase
class UserTests(APITestCase):
    def setUp(self):
        self.casper = Users.objects.create(
            name='Casper', email="casp@gmail.com", password='casper123')
    def test_create_user(self):
        data ={"name":"pam","email":"paaaa@gmail.com","password":"hello"}
        header = {'HTTP_USERNAME': 'admin','HTTP_PASSWORD':'admin1234'}
        response =self.client.post('/users/',data=data, **header)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_list_user(self):
        header = {'HTTP_USERNAME': 'admin', 'HTTP_PASSWORD': 'admin1234'}
        response = self.client.get('/users/',**header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateUserTest(APITestCase):
    def setUp(self):
        #user = Users.objects.create(name="mike", email="Tyson@gmail.com", password="11111")
        pass

    def test_can_update_user(self):
        user = Users.objects.create(name="mike", email="Tyson@gmail.com", password="11111")
        data = UsersSerializer(user).data
        data.update({'name': 'Changed'})
        header = {'HTTP_USERNAME': 'admin', 'HTTP_PASSWORD': 'admin1234'}
        response = self.client.put('/users/1/',data,**header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)






