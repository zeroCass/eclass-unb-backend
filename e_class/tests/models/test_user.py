from django.test import TestCase #type:ignore
from e_class.models import User #type:ignore

"""testando tabela usuário"""
class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)

    def test_user_name_blank(self):
        """Testa se o nome de usuário está vazio"""
        user = User.objects.create(email='test@test',
                                    password='123456',
                                    userType=1)
        self.assertEqual(user.name, '')


    def test_user_email_blank(self):
        """Testa se o email de usuário está vazio"""
        user = User.objects.create(name='test',
                                    password='123456',
                                    userType=1)
        self.assertEqual(user.email, '')

    def test_user_password_blank(self):
        """Testa se a senha de usuário está vazia"""
        user = User.objects.create(name='test',
                                    email='test@test',
                                    userType=1)
        self.assertEqual(user.password, '')

###############################################################################################
        