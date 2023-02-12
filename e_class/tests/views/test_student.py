import json
from django.test import TestCase #type:ignore
from e_class.models import Student #type:ignore
from e_class.serializer import StudentsSerializer
from django.urls import reverse #type: ignore
from rest_framework import status #type: ignore

user = Student()
class GetAllStudentsTest(TestCase):
    """ Teste para buscar todos alunos """

    def setUp(self):
        Student.objects.create(name='aluno1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=3)
        Student.objects.create(name='aluno2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=3)
        Student.objects.create(name='aluno3',
                             email='test3@test',
                             cpf='22222222222',
                             userType=3)
        Student.objects.create(name='aluno4',
                             email='test4@test',
                             cpf='33333333333',
                             userType=3)

    def test_get_all_students(self):
        response = user.get(reverse('get_post_students'))
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleStudentTest(TestCase):
    """ Teste para buscar um aluno """

    def setUp(self):
        self.aluno1 = Student.objects.create(name='aluno1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=3)
        self.aluno2 = Student.objects.create(name='aluno2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=3)
        self.aluno3 = Student.objects.create(name='aluno3',
                             email='test3@test',
                             cpf='22222222222',
                             userType=3)
        self.aluno4 = Student.objects.create(name='aluno4',
                             email='test4@test',
                             cpf='33333333333',
                             userType=3)

    def test_get_valid_single_student(self):
        response = user.get(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno3.pk}))
        student = Student.objects.get(pk=self.aluno3.pk)
        serializer = StudentsSerializer(student)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_student(self):
        response = user.get(
            reverse('get_delete_update_student', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewStudentTest(TestCase):
    """ Teste para criar novo aluno """

    def setUp(self):
        self.valid_payload = {
            'name': 'aluno1',
            'email': 'teste1@test',
            'cpf': '00000000000',
            'userType': 3
        }
        self.invalid_payload = {
            'name': '',
            'email': 'teste1@test',
            'cpf': '00000000000',
            'userType': 3
        }

    def test_create_valid_student(self):
        response = user.post(
            reverse('get_post_students'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        response = user.post(
            reverse('get_post_students'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleStudentTest(TestCase):
    """ Teste para atualizar um aluno já existente """

    def setUp(self):
        self.aluno1 = Student.objects.create(
            name='aluno1', email='test1@test', cpf='00000000000', userType=3)
        self.aluno2 = Student.objects.create(
            name='aluno2', email='test2@test', cpf='11111111111', userType=3)
        self.valid_payload = {
            'name': 'aluno2.0',
            'email': 'test2.0@test',
            'cpf': '11111111111',
            'userType': 3
        }
        self.invalid_payload = {
            'name': '',
            'email': 'test2.0@test',
            'cpf': '11111111111',
            'userType': 3
        }

    def test_valid_update_student(self):
        response = user.put(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_student(self):
        response = user.put(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleStudentTest(TestCase):
    """ Teste para apagar um aluno já existente """

    def setUp(self):
        self.aluno1 = Student.objects.create(
            name='aluno1', email='test1@test', cpf='00000000000', userType=3)
        self.aluno2 = Student.objects.create(
            name='aluno2', email='test2@test', cpf='11111111111', userType=3)

    def test_valid_delete_student(self):
        response = user.delete(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_student(self):
        response = user.delete(
            reverse('get_delete_update_student', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




