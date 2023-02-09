from django.test import TestCase #type:ignore
from e_class.models import Users, Students, Teachers, Admins, Subjects

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
        """Testa se a chave estrangeira do estudante 
        é igual a chave primária de usuário"""
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
        
        Teachers.objects.create(Users_registrationID=User, 
                             specialization='test')

    def test_Teachers_id_fk(self):
        """Testa se a chave estrangeira do professor é 
        igual a chave primária de usuário"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Teacher = Teachers.objects.create(Users_registrationID=User)
        self.assertEqual(Teacher.Users_registrationID.id, 2)

    def test_Teachers_specialization_blank(self):
            """Testa se a especialização está vazia"""
            User = Users.objects.create(name='test',
                                email='test@test',
                                password='123456',
                                userType=1)
            Teacher = Teachers.objects.create(Users_registrationID=User)
            self.assertEqual(Teacher.specialization, '')
            
#################################################################################################

    """testando tabela administrador"""
    def setUpAdmins(self):
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)
        
        Admins.objects.create(Users_registrationID=User)

    def test_Admins_id_fk(self):
        """Testa se a chave estrangeira do administrador
        é igual a chave primária de usuário"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admins.objects.create(Users_registrationID=User)
        self.assertEqual(Admin.Users_registrationID.id, 2)

#################################################################################################

    """testando tabela matérias"""
    def setUpSubjects(self):
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)

        Admin = Admins.objects.create(Users_registrationID=User)

        Subjects.objects.create(course='test', 
                             description='test',
                             Admins_Users_registrationID=Admin)
        
    def test_Subjects_course_blank(self):
        """Testa se o curso está vazio"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admins.objects.create(Users_registrationID=User)

        Subject = Subjects.objects.create(description='test',
                             Admins_Users_registrationID=Admin)

        self.assertEqual(Subject.course, '')

    def test_Subjects_description_blank(self):
        """Testa se a descrição está vazia"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admins.objects.create(Users_registrationID=User)

        Subject = Subjects.objects.create(course='test',
                             Admins_Users_registrationID=Admin)

        self.assertEqual(Subject.description, '')

    def test_Subjects_id_fk(self):
        """Testa se a chave estrangeira de matérias
        é igual a chave primária de admin"""
        User = Users.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admins.objects.create(Users_registrationID=User)

        Subject = Subjects.objects.create(course='test', 
                             description='test',
                             Admins_Users_registrationID=Admin)

        self.assertEqual(Subject.Admins_Users_registrationID.Users_registrationID.id, 2)
        