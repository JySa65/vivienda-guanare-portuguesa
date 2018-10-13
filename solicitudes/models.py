from django.db import models
from usuario.models import Usuario
from departamento.models import Departamento
from sector_zona.models import Estado, Parroquia, Municipio
# Create your models here.


class Solicitud(models.Model):
	numero_de_oficio = models.CharField(max_length=200)
	remitente = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	fecha = models.DateField()
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
	caso_planteado = models.CharField(max_length=200)
	tipo = (
		('1', 'Personal'),
		('2', 'Alto Riezgo'),
		('3', 'Salud'),
		('4', 'Institucional')
	)
	tipo_solicitud = models.CharField(max_length=200, choices=tipo)
	solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE,)

	def __str__(self):
		return '{},{}' .format(self.numero_de_oficio, self.solicitante.nombre)	
