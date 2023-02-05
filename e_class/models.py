from django.db import models

class Users(models.Model):

    class Type(models.IntegerChoices):
        Admins = 1
        Teachers = 2
        Students = 3

    name = models.CharField(max_length=45, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=15, blank=False)
    cpf = models.CharField(max_length=11, blank=True)
    userType = models.IntegerField(choices=Type.choices, blank=False)

    def __str__(self):
        return self.name
