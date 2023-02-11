from django.test import TestCase #type:ignore
from e_class.models import Student #type:ignore

"""testando tabela estudante"""
class StudentModelTest(TestCase):
    def setUp(self):
        Student.objects.create(name='aluno1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=3)
        Student.objects.create(name='aluno2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=3)


    def test_student_unicode(self):
        """Testa se o nome do aluno é o esperado"""
        student1 = Student.objects.get(name='aluno1')
        student2 = Student.objects.get(name='aluno2')
        self.assertEqual(student1.__unicode__(), 'aluno1')
        self.assertEqual(student2.__unicode__(), 'aluno2')