from django.db import models #type:ignore
"""Modelos das tabelas do banco de dados"""

class Users(models.Model):
    'Usuários'
    class Type(models.IntegerChoices):
        Admins = 1
        Teachers = 2
        Students = 3

    name = models.CharField(max_length=45, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=15, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    userType = models.IntegerField(choices=Type.choices, blank=False)

    def __str__(self):
        return str(self.name)

class Students(models.Model):
    'Estudantes'
    Users_registrationID = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.Users_registrationID

    class Meta:
        ordering = ['Users_registrationID']

class Teachers(models.Model):
    'Professores'
    Users_registrationID = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=45, blank=False)

    def __str__(self):
        return self.Users_registrationID

    class Meta:
        ordering = ['Users_registrationID']