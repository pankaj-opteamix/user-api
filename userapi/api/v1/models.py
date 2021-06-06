from django.db import models

# Create your models here.
from django.db import models

class Users(models.Model):
    name  = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

