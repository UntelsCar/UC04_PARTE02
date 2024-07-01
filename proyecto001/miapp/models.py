from django.db import models

# Create your models here.
class Estudiante(models.Model):
    idestudiante = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Codigo")
    dni = models.CharField(max_length=9, unique=True, verbose_name="dni")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    ap_mat = models.CharField(max_length=50, verbose_name="Ap_pat")
    ap_pat = models.CharField(max_length=50, verbose_name="Ap_mat")
    direccion = models.CharField(max_length=150, verbose_name="Direccion")
    telefono = models.CharField(max_length=10, unique=True, verbose_name="Telefono")
    estado = models.BooleanField(default=True, verbose_name="Estado")