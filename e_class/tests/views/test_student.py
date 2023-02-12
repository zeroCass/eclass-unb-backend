import json
from django.test import TestCase #type:ignore
from e_class.models import Student #type:ignore
from e_class.serializer import StudentsSerializer
from django.urls import reverse #type: ignore
from rest_framework import status #type: ignore

user = Student()
class StudentViewTest(TestCase):
    """ Teste para os métodos de alunos """

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

    def test_get_all_students(self):
        """ Teste para buscar todos alunos """
        response = user.get(reverse('get_post_students'))
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_student(self):
        """ Teste válido para buscar um aluno """
        response = user.get(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno3.pk}))
        student = Student.objects.get(pk=self.aluno3.pk)
        serializer = StudentsSerializer(student)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_student(self):
        """ Teste inválido para buscar um aluno """
        response = user.get(
            reverse('get_delete_update_student', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_student(self):
        """ Teste válido para criar novo aluno """
        response = user.post(
            reverse('get_post_students'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        """ Teste inválido para criar novo aluno """
        response = user.post(
            reverse('get_post_students'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_student(self):
        """ Teste válido para atualizar um aluno já existente """
        response = user.put(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_student(self):
        """ Teste inválido para atualizar um aluno já existente """
        response = user.put(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_student(self):
        """ Teste válido para apagar um aluno já existente """
        response = user.delete(
            reverse('get_delete_update_student', kwargs={'pk': self.aluno2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_student(self):
        """ Teste inválido para apagar um aluno já existente """
        response = user.delete(
            reverse('get_delete_update_student', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
