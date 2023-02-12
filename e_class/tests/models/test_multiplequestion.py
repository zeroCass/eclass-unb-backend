from django.test import TestCase #type:ignore
from e_class.models import MultipleQuestion, Teacher #type:ignore

"""testando tabela questão de múltipla escolha"""
class MultipleQuestionModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(name='professor1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=2)
        Teacher.objects.create(name='professor2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=2)
        MultipleQuestion.objects.create(name='Questão Kanban',
                                        answer=1,
                                        teacher_id=1)
        MultipleQuestion.objects.create(name='Questão Scrum',
                                        answer=2,
                                        teacher_id=2)


    def test_MultipleQuestion_unicode(self):
        """Testa se o nome da questão de múltipla escolha é o esperado"""
        multipleQuestion1 = MultipleQuestion.objects.get(name='Questão Kanban')
        multipleQuestion2 = MultipleQuestion.objects.get(name='Questão Scrum')
        self.assertEqual(multipleQuestion1.__unicode__(), 'Questão Kanban')
        self.assertEqual(multipleQuestion2.__unicode__(), 'Questão Scrum')