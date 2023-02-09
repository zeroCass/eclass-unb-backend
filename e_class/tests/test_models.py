from django.test import TestCase #type:ignore
from e_class.models import Users, Students

"""teste todas as tabelas do bd"""
class ClassTestCase(TestCase):
    """teste da tabela usuário"""
    "testando usuário "
    def setUp(self):
        Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)

    def test_user_name_blank(self):
        """Testa se o nome de usuário está vazio"""
        user = Users.objects.create(email='test@test',
                                    password='123456',
                                    userType=1)
        self.assertEqual(user.name, '')


    def test_user_email_blank(self):
        """Testa se o email de usuário está vazio"""
        user = Users.objects.create(name='test',
                                    password='123456',
                                    userType=1)
        self.assertEqual(user.email, '')

    def test_user_password_blank(self):
        """Testa se a senha de usuário está vazia"""
        user = Users.objects.create(name='test',
                                    email='test@test',
                                    userType=1)
        self.assertEqual(user.password, '')

#################################################################################################

    """testando tabela estudante"""
    def setUpStudents(self):
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)
        
        Students.objects.create(Users_registrationID=User)

    def test_Student_id_fk(self):
        """Testa se a chave estrangeira do estudante é 5"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Student = Students.objects.create(Users_registrationID=User)
        self.assertEqual(Student.Users_registrationID.id, 2)

#################################################################################################
    
    """testando tabela Professor"""    
    def setUpTeachers(self):
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)
        
        Teachers.objects.create(Users_registrationID=User)

    def test_Teachers_id_fk(self):
        """Testa se a chave estrangeira do professor é 5"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Teacher = Teachers.objects.create(Users_registrationID=User)
        self.assertEqual(Teachers.Users_registrationID.id, 2)
