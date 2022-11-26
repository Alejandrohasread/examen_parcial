from django.db import models

# Create your models here.
class usuario(models.Model):
    nombres = models.CharField(max_length=64,default='')
    apellidos = models.CharField(max_length=64,default='')
    codigo_usuario = models.CharField(max_length=64,default='')
    clave = models.CharField(max_length=64,default='')

class tarea(models.Model):
    titulo = models.CharField(max_length=64,default='')
    descripcion = models.CharField(max_length=128,default='')
    fecha_creacion = models.CharField(max_length=96,default='')
    fecha_entrega = models.CharField(max_length=96,default='')
    usuario_designado = models.CharField(max_length=64,default='')