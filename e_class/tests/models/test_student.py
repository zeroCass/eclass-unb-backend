from django.test import TestCase #type:ignore
from e_class.models import Student #type:ignore

"""testando tabela estudante"""
class StudentModelTest(TestCase):
    def setUpStudents(self):
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)
        
        Student.objects.create(Users_registrationID=User)

    def test_Student_id_fk(self):
        """Testa se a chave estrangeira do estudante 
        é igual a chave primária de usuário"""
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Student = Student.objects.create(Users_registrationID=User)
        self.assertEqual(Student.Users_registrationID.id, 2)