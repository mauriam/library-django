from django.db import models

class AutorModel(models.Model):
    firtname = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Primer Nombre')
    lastname = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Segundo Nombre')
    nationality = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Nacionalidad')
    descriptions = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Descipcion')
