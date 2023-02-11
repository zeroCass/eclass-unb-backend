from django.test import TestCase #type:ignore
from e_class.models import Admin #type:ignore

"""testando tabela administrador"""
class AdminModelTest(TestCase):  
    def setUp(self):
        Admin.objects.create(name='administrador1',
                             email='test1@test',
                             cpf='00000000000',
                             userType=1)
        Admin.objects.create(name='administrador2',
                             email='test2@test',
                             cpf='11111111111',
                             userType=1)

    def test_admin_unicode(self):
        """Testa se o nome do administrador é o esperado"""
        admin1 = Admin.objects.get(name='administrador1')
        admin2 = Admin.objects.get(name='administrador2')
        self.assertEqual(admin1.__unicode__(), 'administrador1')
        self.assertEqual(admin2.__unicode__(), 'administrador2')

    
    