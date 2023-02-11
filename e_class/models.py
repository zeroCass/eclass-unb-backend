from django.db import models  # type:ignore


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
    "Administrador"

    class Meta:
        ordering = ["name"]


class Teacher(User):
    "Professor"

    specialization = models.CharField(max_length=45)

    class Meta:
        ordering = ["name"]


class Student(User):
    "Estudante"

    class Meta:
        ordering = ["name"]


class Subject(models.Model):
    "Materia"

    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    teachers = models.ManyToManyField(Teacher)
    course = models.CharField(max_length=45, unique=True)
    description = models.TextField(max_length=200)

    def __unicode__(self):
        return self.course

    class Meta:
        ordering = ["course"]


class Classes(models.Model):
    "Turma"

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through="Students_has_Classes")
    teachers = models.ManyToManyField(Teacher)
    name = models.CharField(max_length=15)
    size = models.IntegerField()
    startTime = models.DateField()
    endTime = models.DateField()
    period = models.IntegerField()
    password = models.CharField(max_length=30)
    createdAt = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Students_has_Classes(models.Model):
    "Tabela intermedária entre Estudante e Turma"

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    registerDate = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["registerDate"]


class Question(models.Model):
    "Questões"

    is_visibility = models.BooleanField(default=False)
    statement = models.TextField()
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ["statement"]


class MultipleQuestion(Question):
    "Questão múltipla escolha"
    
    answerChoices = ((1, "Option1"), (2, "Option2"), (3, "Option3"), (4, "Option4"))
    
    id = models.AutoField(primary_key=True)
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField(null=True)
    option4 = models.TextField(null=True)
    answer = models.IntegerField(choices=answerChoices)

    class Meta:
        ordering = ["id"]


class DiscursiveQuestion(models.Model):
    "Questão discursiva"

    id = models.AutoField(primary_key=True)
    answer = models.TextField(max_lenght="200", null=True)

    class Meta:
        ordering = ["id"]


class Exams(models.Model):
    "Exame"

    id = models.AutoField(primary_key=True)
    startAt = models.DateTimeField()
    endedAt = models.DateTimeField()
    isVisible = models.BooleanField()
    score = models.FloatField()
    multipleQuestions = models.ManyToManyField(MultipleQuestion)
    discursiveQuestions = models.ManyToManyField(DiscursiveQuestion)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
