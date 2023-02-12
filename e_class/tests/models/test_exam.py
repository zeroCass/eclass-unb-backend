from django.test import TestCase #type:ignore
from e_class.models import Exams, Teacher #type:ignore

"""testando tabela prova"""
class ExamsModelTest(TestCase):
    def setUp(self):
        Teacher.objects.create(name='professor1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=2)
        Teacher.objects.create(name='professor2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=2)
        Exams.objects.create(name='Prova 2022/1',
                             startAt='2022-02-02',
                             endedAt='2022-02-13',
                             isVisible=True,
                             score=10.0,
                             teacher_id=1)
        Exams.objects.create(name='Prova 2022/2',
                             startAt='2022-02-03',
                             endedAt='2022-02-14',
                             isVisible=False,
                             score=9.0,
                             teacher_id=2)


    def test_Exam_unicode(self):
        """Testa se o nome da prova é o esperado"""
        exam1 = Exams.objects.get(name='Prova 2022/1')
        exam2 = Exams.objects.get(name='Prova 2022/2')
        self.assertEqual(exam1.__unicode__(), 'Prova 2022/1')
        self.assertEqual(exam2.__unicode__(), 'Prova 2022/2')