from django.db import models
from usuario.models import Usuario
# Create your models here.


class Departamento(models.Model):
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class Cargo(models.Model):
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class Trabajador(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.nombre
