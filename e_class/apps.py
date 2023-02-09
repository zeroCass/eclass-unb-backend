'app py file'
from django.apps import AppConfig # type:ignore

class EClassConfig(AppConfig):
    """settings of eclass"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_class'
