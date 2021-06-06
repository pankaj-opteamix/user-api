from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
class UserAPITests(APITestCase):
    def tetscreate_User(self):
        data ={"name":"johny","email":"paaaa@gmail.com","password":"hello"}
        response =self.client.post('/users/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)