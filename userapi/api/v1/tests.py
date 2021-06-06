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
            name='Casper', email="john@gmail.com", password='Bull Dog')
    def test_create_user(self):
        print("hello")
        data ={"name":"johny","email":"paaaa@gmail.com","password":"hello"}
        header = {'HTTP_USERNAME': 'P'}
        response =self.client.post('/users/',data=data, **header)
        print(response.status_code)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_list_user(self):
        header = {'HTTP_USERNAME': 'P'}
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateUserTest(APITestCase):
    def setUp(self):
        pass

    def test_can_update_user(self):
        user = Users.objects.create(name="mike", email="Tyson@gmail.com", password="11111")
        data = UsersSerializer(user).data
        data.update({'name': 'Changed'})

        response = self.client.put('/users/1/',data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteUserTest(APITestCase):
    def setUp(self):
        pass

    def Delete_can_update_user(self):
        user = Users.objects.create(name="mike", email="Tyson@gmail.com", password="11111")
        data = UsersSerializer(user).data
        data.update({'name': 'Changed'})

        response = self.client.put('/users/1/',data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)






