from django.test import TestCase #type:ignore
from e_class.models import Subject #type:ignore

"""testando tabela usuário"""
class SubjectModelTest(TestCase):
    def setUpSubjects(self):
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)

        Admin = Admin.objects.create(Users_registrationID=User)

        Subject.objects.create(course='test', 
                             description='test',
                             Admins_Users_registrationID=Admin)
        
    def test_Subjects_course_blank(self):
        """Testa se o curso está vazio"""
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admin.objects.create(Users_registrationID=User)

        Subject = Subject.objects.create(description='test',
                             Admins_Users_registrationID=Admin)

        self.assertEqual(Subject.course, '')

    def test_Subjects_description_blank(self):
        """Testa se a descrição está vazia"""
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admin.objects.create(Users_registrationID=User)

        Subject = Subject.objects.create(course='test',
                             Admins_Users_registrationID=Admin)

        self.assertEqual(Subject.description, '')

    def test_Subjects_id_fk(self):
        """Testa se a chave estrangeira de matérias
        é igual a chave primária de admin"""
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admin.objects.create(Users_registrationID=User)

        Subject = Subject.objects.create(course='test', 
                             description='test',
                             Admins_Users_registrationID=Admin)

        self.assertEqual(Subject.Admins_Users_registrationID.Users_registrationID.id, 2)