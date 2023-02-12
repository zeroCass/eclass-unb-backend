import json
from django.test import TestCase #type:ignore
from e_class.models import Teacher #type:ignore
from e_class.serializer import TeachersSerializer
from django.urls import reverse #type: ignore
from rest_framework import status #type: ignore

user = Teacher()
class GetAllTeacherTest(TestCase):
    """ Teste para buscar todos professores """

    def setUp(self):
        Teacher.objects.create(name='professor1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=3)
        Teacher.objects.create(name='professor2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=3)
        Teacher.objects.create(name='professor3',
                             email='test3@test',
                             cpf='22222222222',
                             userType=3)
        Teacher.objects.create(name='professor4',
                             email='test4@test',
                             cpf='33333333333',
                             userType=3)

    def test_get_all_teachers(self):
        response = user.get(reverse('get_post_teachers'))
        teachers = Teacher.objects.all()
        serializer = TeachersSerializer(teachers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleTeacherTest(TestCase):
    """ Teste para buscar um professor """

    def setUp(self):
        self.professor1 = Teacher.objects.create(name='professor1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=3)
        self.professor2 = Teacher.objects.create(name='professor2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=3)
        self.professor3 = Teacher.objects.create(name='professor3',
                             email='test3@test',
                             cpf='22222222222',
                             userType=3)
        self.professor4 = Teacher.objects.create(name='professor4',
                             email='test4@test',
                             cpf='33333333333',
                             userType=3)

    def test_get_valid_single_teacher(self):
        response = user.get(
            reverse('get_delete_update_teacher', kwargs={'pk': self.professor3.pk}))
        teacher = Teacher.objects.get(pk=self.professor3.pk)
        serializer = TeachersSerializer(teacher)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_teacher(self):
        response = user.get(
            reverse('get_delete_update_teacher', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewTeacherTest(TestCase):
    """ Teste para criar novo professor """

    def setUp(self):
        self.valid_payload = {
            'name': 'professor1',
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

    def test_create_valid_teacher(self):
        response = user.post(
            reverse('get_post_teachers'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_teacher(self):
        response = user.post(
            reverse('get_post_teachers'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleTeacherTest(TestCase):
    """ Teste para atualizar um professor já existente """

    def setUp(self):
        self.professor1 = Teacher.objects.create(
            name='professor1', email='test1@test', cpf='00000000000', userType=3)
        self.professor2 = Teacher.objects.create(
            name='professor2', email='test2@test', cpf='11111111111', userType=3)
        self.valid_payload = {
            'name': 'professor2.0',
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

    def test_valid_update_teacher(self):
        response = user.put(
            reverse('get_delete_update_teacher', kwargs={'pk': self.professor2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_teacher(self):
        response = user.put(
            reverse('get_delete_update_teacher', kwargs={'pk': self.professor2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTeacherTest(TestCase):
    """ Teste para apagar um professor já existente """

    def setUp(self):
        self.professor1 = Teacher.objects.create(
            name='professor1', email='test1@test', cpf='00000000000', userType=3)
        self.professor2 = Teacher.objects.create(
            name='professor2', email='test2@test', cpf='11111111111', userType=3)

    def test_valid_delete_teacher(self):
        response = user.delete(
            reverse('get_delete_update_teacher', kwargs={'pk': self.professor2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_teacher(self):
        response = user.delete(
            reverse('get_delete_update_teacher', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
