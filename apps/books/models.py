from django.db import models

class AutorModel(models.Model):
    firstname = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Nombre')
    lastname = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Apellido')
    nationality = models.CharField(max_length = 30, blank = False, null = False, verbose_name = 'Nacionalidad')
    descriptions = models.CharField(max_length = 300, blank = False, null = False, verbose_name = 'Descipcion')
    create_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = 'Fecha de Registro' )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    def __str__(self):
        return  self.lastname+' '+self.firstname

class BookModel(models.Model):
    title = models.CharField('Titulo', max_length = 255, blank = False, null = False)
    publication_date = models.DateField('Fecha de Publicacion', blank = False, null = False )
    fk_autor = models.ManyToManyField(AutorModel)
    create_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = 'Fecha de Registro' )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.title