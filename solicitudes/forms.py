from django import forms
from usuario.models import *
from solicitudes.models import *


class SolicitanteForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('tipo_cedula', 'cedula', 'nombre',
                  'apellido', 'telefono', 'fecha_nacimiento',
                  'correo', 'direccion')


class SolicitudForm(forms.ModelForm):
    solicitante = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(
                    is_solicitante=True).order_by('-created_at'), 
        widget=forms.Select(), 
        )
    
    class Meta:
        model = Solicitud
        fields = ('solicitante', 'tipo_solicitud', 'numero_de_oficio', 'remitente',
                  'fecha', 'estado', 'municipio', 'parroquia', 'caso_planteado')
