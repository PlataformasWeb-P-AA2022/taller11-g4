from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from viviendas.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese cédula por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        nombre_ciudad = valor.split()
        primera_letra = nombre_ciudad[0]

        if primera_letra[0] == 'L':
            raise forms.ValidationError("El nombre de la ciudad no puede empezar con la letra mayuscula 'L'")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo_departamento', 'num_cuartos']

    def clean_costo_departamento(self):
        valor = self.cleaned_data['costo_departamento']
        if len(valor) > 1000:
            raise forms.ValidationError("EL costo del departamento no puede ser mayor a $100 000")
        return valor
    
    def clean_num_departamentos(self):
        valor = self.cleaned_data['num_departamentos']
        if len(valor) != 0 and len(valor) > 7:
            raise forms.ValidationError("El numero de cuartos no puede ser 0 ni mayor a 7")
        return valor

    def clean_num_departamentos(self):
        valor = self.cleaned_data['nombre_propietario']
        nombre = len(valor.split())
        if nombre < 3:
            raise forms.ValidationError("El nombre completo del propietario no puede tener ser menor a 3 palabras")
        return valor

s
class NumeroTelefonicoEstudianteForm(ModelForm):

    def __init__(self, estudiante, *args, **kwargs):
        super(NumeroTelefonicoEstudianteForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        print(estudiante)

    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante', 'costo_plan']
