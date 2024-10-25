from django import forms
from .models import Vehiculo

#creating a form
class VehiculoForm(forms.ModelForm):

    #create meta class
    class Meta:
        #specify model to be used
        model = Vehiculo

        #specify fields to be used
        fields = [
            "placa",
            "marca",
            "modelo",
            "color_vehiculo",
        ]

        labels = {
            'placa': 'Numero de Placa',
            'marca': 'Marca del Vehiculo',
            'modelo': 'Modelo del Vehiculo',
            'color_vehiculo': 'Color del Vehiculo',
        } 

        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }