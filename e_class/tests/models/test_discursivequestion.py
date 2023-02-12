from django.test import TestCase #type:ignore
from e_class.models import DiscursiveQuestion, Teacher #type:ignore

"""testando tabela questão discursiva"""
class DiscursiveQuestionModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(name='professor1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=2)
        Teacher.objects.create(name='professor2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=2)
        DiscursiveQuestion.objects.create(name='Questão Kanban',
                                        teacher_id=1)
        DiscursiveQuestion.objects.create(name='Questão Scrum',
                                        teacher_id=2)


    def test_DiscursiveQuestion_unicode(self):
        """Testa se o nome da questão discursiva é o esperado"""
        DiscursiveQuestion1 = DiscursiveQuestion.objects.get(name='Questão Kanban')
        DiscursiveQuestion2 = DiscursiveQuestion.objects.get(name='Questão Scrum')
        self.assertEqual(DiscursiveQuestion1.__unicode__(), 'Questão Kanban')
        self.assertEqual(DiscursiveQuestion2.__unicode__(), 'Questão Scrum')