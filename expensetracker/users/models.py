from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact = models.BigIntegerField(null=False)

    def __str__(self):
        return self.username
