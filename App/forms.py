from django import forms 

class ParticipanteForm(forms.Form):
    nombre = forms.CharField(max_length=20,required=True)
    apellido = forms.CharField(max_length=20,required=True)
    edad = forms.IntegerField(required=True)

class LibroForm(forms.Form):
    nombre = forms.CharField(max_length=20,required=True)
    cantidadLetras = forms.IntegerField(required=True)

class CalificacionForm(forms.Form):
    nota = forms.IntegerField(required=True)
    nombreJurado= forms.CharField(max_length=20,required=True)
    nombreLibro = forms.CharField(max_length=20, required=True)