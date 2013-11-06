from django import forms

class SubirDocumentoForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    contenido  = forms.FileField()
    destino = forms.CharField(max_length=200)
    


