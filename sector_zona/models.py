from django.db import models

# Create your models here.


class Estado(models.Model):
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=1000)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Parroquia(models.Model):
    nombre = models.CharField(max_length=1000)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
