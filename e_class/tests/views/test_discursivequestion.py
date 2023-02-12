import json
from django.test import TestCase #type:ignore
from e_class.models import DiscursiveQuestion, Teacher #type:ignore
from ...serializers.questions_serializer import DiscursiveQuestionSerializer
from django.urls import reverse #type:ignore
from rest_framework import status #type:ignore

question = DiscursiveQuestion()
class DiscursiveQuestionViewTest(TestCase):
    """ Teste para os métodos de questão discursiva """

    def setUp(self):
        Teacher.objects.create(name='professor1',
                               email='test1@test',
                               cpf='00000000000',
                               userType=2)
        Teacher.objects.create(name='professor2',
                               email='test2@test',
                               cpf='11111111111',
                               userType=2)
        Teacher.objects.create(name='professor3',
                               email='test3@test',
                               cpf='22222222222',
                               userType=2)
        Teacher.objects.create(name='professor4',
                               email='test4@test',
                               cpf='33333333333',
                               userType=2)
        self.questão1 = DiscursiveQuestion.objects.create(name='Questão Kanban',
                                                          teacher_id=1)
        self.questão2 = DiscursiveQuestion.objects.create(name='Questão Scrum',
                                                          teacher_id=2)
        self.questão3 = DiscursiveQuestion.objects.create(name='Questão Casos de Uso',
                                                          teacher_id=3)
        self.questão4 = DiscursiveQuestion.objects.create(name='Questão DFD',
                                                          teacher_id=4)
        self.valid_payload = {
            'name': 'Questão Kanban 2.0',
            'teacher_id': 1
        }
        self.invalid_payload = {
            'name': 'Questão Kanban 2.0',
            'teacher_id': -1
        }

    def test_get_all_discursiveQuestions(self):
        """ Teste para buscar todas as questões discursivas """
        response = question.get(reverse('get_post_discursiveQuestions'))
        discursiveQuestions = DiscursiveQuestion.objects.all()
        serializer = DiscursiveQuestionSerializer(discursiveQuestions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_discursiveQuestion(self):
        """ Teste válido para buscar uma questão discursiva """
        response = question.get(
            reverse('get_delete_update_discursiveQuestion', kwargs={'pk': self.questão3.pk}))
        DiscursiveQuestion = DiscursiveQuestion.objects.get(pk=self.questão3.pk)
        serializer = DiscursiveQuestionSerializer(DiscursiveQuestion)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_discursiveQuestion(self):
        """ Teste inválido para buscar uma questão discursiva"""
        response = question.get(
            reverse('get_delete_update_discursiveQuestion', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_discursiveQuestion(self):
        """ Teste válido para criar nova questão discursiva """
        response = question.post(
            reverse('get_post_discursiveQuestions'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_discursiveQuestion(self):
        """ Teste inválido para criar nova questão discursiva """
        response = question.post(
            reverse('get_post_discursiveQuestions'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_discursiveQuestion(self):
        """ Teste válido para atualizar uma questão discursiva já existente """
        response = question.put(
            reverse('get_delete_update_discursiveQuestion', kwargs={'pk': self.questão2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_discursiveQuestion(self):
        """ Teste inválido para atualizar uma questão discursiva já existente """
        response = question.put(
            reverse('get_delete_update_discursiveQuestion', kwargs={'pk': self.questão2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_discursiveQuestion(self):
        """ Teste válido para apagar um questão discursiva já existente """
        response = question.delete(
            reverse('get_delete_update_discursiveQuestion', kwargs={'pk': self.questão2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_discursiveQuestion(self):
        """ Teste inválido para apagar um questão discursiva já existente """
        response = question.delete(
            reverse('get_delete_update_discursiveQuestion', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
