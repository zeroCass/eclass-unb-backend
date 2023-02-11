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
    admin = models.ForeignKey(Admin, on_delete=models.PROTECT)
    teachers = models.ManyToManyField(Teacher)
    course = models.CharField(max_length=45, unique=True)
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return self.course

    class Meta:
        ordering = ["course"]

class Classes(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through="Students_has_Classes")
    name = models.CharField(max_length=15)
    size = models.IntegerField()
    startTime = models.DateField()
    endTime = models.DateField()
    period = models.IntegerField()
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Students_has_Classes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    registerDate = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["registerDate"]