from django import forms
from sector_zona.models import Estado, Municipio, Parroquia

class EstadoForm(forms.ModelForm):

    class Meta:
        model = Estado
        fields = ('nombre',)


class MunicipioForm(forms.ModelForm):

    class Meta:
        model = Municipio
        fields = ('nombre', 'municipio')


class ParroquiaForm(forms.ModelForm):

    class Meta:
        model = Parroquia
        fields = ('nombre', 'municipio')
