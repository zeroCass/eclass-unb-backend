import json
from django.test import TestCase #type:ignore
from e_class.models import MultipleQuestion, Teacher #type:ignore
from e_class.serializer import MultipleQuestionSerializer
from django.urls import reverse
from rest_framework import status

question = MultipleQuestion()
class MultipleQuestionViewTest(TestCase):
    """ Teste para os métodos de questão de múltipla escolha """

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
        self.questão1 = MultipleQuestion.objects.create(name='Questão Kanban',
                                                        answer=1,
                                                        teacher_id=1)
        self.questão2 = MultipleQuestion.objects.create(name='Questão Scrum',
                                                        answer=2,
                                                        teacher_id=2)
        self.questão3 = MultipleQuestion.objects.create(name='Questão Casos de Uso',
                                                        answer=1,
                                                        teacher_id=3)
        self.questão4 = MultipleQuestion.objects.create(name='Questão DFD',
                                                        answer=2,
                                                        teacher_id=4)
        self.valid_payload = {
            'name': 'Questão Kanban 2.0',
            'answer': 1,
            'teacher_id': 1
        }
        self.invalid_payload = {
            'name': 'Questão Kanban 2.0',
            'answer': 1,
            'teacher_id': -1
        }

    def test_get_all_multipleQuestions(self):
        """ Teste para buscar todas as questões de múltipla escolha  """
        response = question.get(reverse('get_post_multipleQuestions'))
        multipleQuestions = MultipleQuestion.objects.all()
        serializer = MultipleQuestionSerializer(multipleQuestions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_multipleQuestion(self):
        """ Teste válido para buscar uma questão de múltipla escolha  """
        response = question.get(
            reverse('get_delete_update_multipleQuestion', kwargs={'pk': self.questão3.pk}))
        multipleQuestion = MultipleQuestion.objects.get(pk=self.questão3.pk)
        serializer = MultipleQuestionSerializer(multipleQuestion)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_multipleQuestion(self):
        """ Teste inválido para buscar uma questão de múltipla escolha """
        response = question.get(
            reverse('get_delete_update_multipleQuestion', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_multipleQuestion(self):
        """ Teste válido para criar nova questão de múltipla escolha  """
        response = question.post(
            reverse('get_post_multipleQuestions'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_multipleQuestion(self):
        """ Teste inválido para criar nova questão de múltipla escolha """
        response = question.post(
            reverse('get_post_multipleQuestions'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_multipleQuestion(self):
        """ Teste válido para atualizar uma questão de múltipla escolha já existente """
        response = question.put(
            reverse('get_delete_update_multipleQuestion', kwargs={'pk': self.questão2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_multipleQuestion(self):
        """ Teste inválido para atualizar uma questão de múltipla escolha já existente """
        response = question.put(
            reverse('get_delete_update_multipleQuestion', kwargs={'pk': self.questão2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_multipleQuestion(self):
        """ Teste válido para apagar um questão de múltipla escolha já existente """
        response = question.delete(
            reverse('get_delete_update_multipleQuestion', kwargs={'pk': self.questão2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_multipleQuestion(self):
        """ Teste inválido para apagar um questão de múltipla escolha já existente """
        response = question.delete(
            reverse('get_delete_update_multipleQuestion', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
