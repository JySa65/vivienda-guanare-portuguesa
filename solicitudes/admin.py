from django.contrib import admin
from .models import Solicitud

# Register your models here.


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('numero_de_oficio', 'tipo_solicitud', 'solicitante')
