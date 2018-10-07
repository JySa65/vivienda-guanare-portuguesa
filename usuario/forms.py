from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuario import models


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = models.Usuario
        fields = ('tipo_cedula', 'cedula', 'nombre',
                  'apellido', 'telefono', 'fecha_nacimiento',
                  'correo', 'direccion')


class UsuarioActualizarForm(forms.ModelForm):
    tipo_cedula = forms.ChoiceField(choices=(('V', 'V'), ('E', 'E')), disabled=True)
    cedula = forms.CharField(disabled=True)
    class Meta:
        model = models.Usuario
        fields = ('tipo_cedula', 'cedula', 'nombre',
                  'apellido', 'telefono', 'fecha_nacimiento',
                  'correo', 'direccion')
