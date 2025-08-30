from django import forms

class FormularioBaseComputadora(forms.Form):
    marca = forms.CharField(max_length=20)

class FormularioCrearComputadora(FormularioBaseComputadora):
    modelo = forms.CharField(max_length=20)
    imagen = forms.ImageField(required=False)

class FormularioBuscarComputadora(FormularioBaseComputadora):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)