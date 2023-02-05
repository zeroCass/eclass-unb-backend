from django.test import TestCase
from e_class.models import Users

class UsersTestCase(TestCase):
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
        self.assertEqual(user.email, ''):
            

    def test_user_password_blank(self):
        """Testa se a senha de usuário está vazia"""
        user = Users.objects.create(name='test',
                                    email='test@test',
                                    userType=1)
        self.assertEqual(user.password, '')
        