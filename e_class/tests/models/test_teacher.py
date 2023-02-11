from django.test import TestCase #type:ignore
from e_class.models import Teacher #type:ignore

"""testando tabela professor"""
class TeacherModelTest(TestCase):  
    def setUpTeachers(self):
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)
        
        Teacher.objects.create(Users_registrationID=User, 
                             specialization='test')

    def test_Teachers_id_fk(self):
        """Testa se a chave estrangeira do professor é 
        igual a chave primária de usuário"""
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Teacher = Teacher.objects.create(Users_registrationID=User)
        self.assertEqual(Teacher.Users_registrationID.id, 2)

    def test_Teachers_specialization_blank(self):
            """Testa se a especialização está vazia"""
            User = User.objects.create(name='test',
                                email='test@test',
                                password='123456',
                                userType=1)
            Teacher = Teacher.objects.create(Users_registrationID=User)
            self.assertEqual(Teacher.specialization, '')