from django.test import TestCase #type:ignore
from e_class.models import Subject #type:ignore

"""testando tabela usuário"""
class SubjectModelTest(TestCase):
    def setUp(self):
        Subject.objects.create(name='matemática')
        Subject.objects.create(name='português')

    def test_subject_unicode(self):
        """Testa se o curso da matéria é o esperado"""
        subject1 = Subject.objects.get(name='matemática')
        subject2 = Subject.objects.get(name='português')
        self.assertEqual(subject1.__unicode__(), 'matemática')
        self.assertEqual(subject2.__unicode__(), 'português')