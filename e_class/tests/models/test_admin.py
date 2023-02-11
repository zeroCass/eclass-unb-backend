from django.test import TestCase #type:ignore
from e_class.models import Admin #type:ignore

"""testando tabela administrador"""
class AdminModelTest(TestCase):  
    def setUpAdmins(self):
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1,
                             id=5)
        
        Admin.objects.create(Users_registrationID=User)

    def test_Admins_id_fk(self):
        """Testa se a chave estrangeira do administrador
        é igual a chave primária de usuário"""
        User = User.objects.create(name='test',
                             email='test@test',
                             password='123456',
                             userType=1)
        Admin = Admin.objects.create(Users_registrationID=User)
        self.assertEqual(Admin.Users_registrationID.id, 2)