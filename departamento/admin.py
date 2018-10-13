from django.contrib import admin
from departamento.models import Departamento, Cargo, Trabajador
# Register your models here.

admin.site.register(Departamento)
admin.site.register(Cargo)
admin.site.register(Trabajador)
