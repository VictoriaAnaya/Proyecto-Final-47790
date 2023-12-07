from django import forms

from . import models

class Usuario_Form(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["nombre", 
                  "apellido", 
                  "nacimiento", 
                  "intereses", 
                  "pais_origen"]

    pais_origen = forms.ModelChoiceField(queryset=models.Pais.objects.all())

class Noticia_Form(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = ["titulo", 
                  "contenido", 
                  "categoria",
                  "autor"]

    categoria = forms.ModelChoiceField(queryset=models.Categoria.objects.all())