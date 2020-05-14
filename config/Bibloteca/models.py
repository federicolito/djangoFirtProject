from django.db import models
from django.db import models

# Create your models here.

class Autor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return "Autor {}  {} ".format(self.codigo, self.nombre)

class Libro(models.Model):
    codigo = models.AutoField(primary_key=True)
    codAutor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=25)
    editorial = models.CharField(max_length=25)
    cantidadPaginas = models.IntegerField()

    def __str__(self):
        return "Libro {} {} {} {} {}".format(self.codigo, self.codAutor, self.titulo, self.editorial,self.cantidadPaginas)

class Ejemplar(models.Model):
    codigo = models.AutoField(primary_key=True)
    #codUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")
    codLibro = models.ForeignKey(Libro, on_delete=models.CASCADE, default="")
    localizacion = models.CharField(max_length=25)
    
    def __str__(self):
        return "Ejemplar {} {} {} {}".format(self.codigo, self.codUsuario, self.codLibro, self.localizacion) 

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    ejemplares = models.ManyToManyField(Ejemplar)

    def __str__(self):
        return "Usuario {} {} {} {}".format(self.codigo, self.nombre, self.telefono, self.direccion)

