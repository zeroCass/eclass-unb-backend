from django.db import models  # type:ignore

"""Modelos das tabelas do banco de dados"""


class User(models.Model):
    "Usuário"

    userTypeChoices = ((1, "Admin"), (2, "Teacher"), (3, "Student"))

    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    userType = models.IntegerField(choices=userTypeChoices)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Admin(User):
    class Meta:
        ordering = ["name"]


class Teacher(User):
    specialization = models.CharField(max_length=45)

    class Meta:
        ordering = ["name"]


class Student(User):
    class Meta:
        ordering = ["name"]


class Subject(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete=models.PROTECT)
    course = models.CharField(max_length=45, unique=True)
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return self.course

    class Meta:
        ordering = ["course"]
