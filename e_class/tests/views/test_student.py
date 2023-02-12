import json
from django.test import TestCase #type:ignore
from ...models import Student #type:ignore
from ...serializers.students_serializer import StudentsSerializer, StudentsSerializerEDIT
from ...views.view_students import studentOne, studentsList
from ...urls import *
from django.urls import reverse #type: ignore
from rest_framework import status #type: ignore

users = studentsList()
user = studentOne()
class StudentViewTest(TestCase):
    """ Teste para os métodos de alunos """

    def setUp(self):
        self.aluno1 = Student.objects.create(name='aluno1',
                             email='test1@test',
                             password='123456',
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

    def test_get_studentsList(self):
        """ Teste para buscar todos alunos """
        response = users.get()
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_studentOne(self):
        """ Teste válido para buscar um aluno """
        response = user.get(self.aluno3.pk)
        student = Student.objects.get(pk=self.aluno3.pk)
        serializer = StudentsSerializer(student)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_studentOne(self):
        """ Teste inválido para buscar um aluno """
        response = user.getObject(30)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_studentList(self):
        """ Teste válido para criar novo aluno """
        response = users.post(self.valid_payload.items)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_studentList(self):
        """ Teste inválido para criar novo aluno """
        response = user.post(data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_studentOne(self):
        """ Teste válido para atualizar um aluno já existente """
        response = user.put(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_studentOne(self):
        """ Teste inválido para atualizar um aluno já existente """
        response = user.put(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_studentOne(self):
        """ Teste válido para apagar um aluno já existente """
        response = user.delete(self.aluno2.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_studentOne(self):
        """ Teste inválido para apagar um aluno já existente """
        response = user.delete(30)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
