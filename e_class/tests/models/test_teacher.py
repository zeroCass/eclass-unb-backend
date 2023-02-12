from django.test import TestCase #type:ignore
from e_class.models import Teacher #type:ignore

"""testando tabela professor"""
class TeacherModelTest(TestCase):  
    def setUp(self):
        Teacher.objects.create(name='professor1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=2)
        Teacher.objects.create(name='professor2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=2)


    def test_teacher_unicode(self):
        """Testa se o nome do professor é o esperado"""
        teacher1 = Teacher.objects.get(name='professor1')
        teacher2 = Teacher.objects.get(name='professor2')
        self.assertEqual(teacher1.__unicode__(), 'professor1')
        self.assertEqual(teacher2.__unicode__(), 'professor2')