from django import forms

from . import models

class Usuario_Form(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["id", "nombre", "apellido", "nacimiento", "intereses", "pais_origen"]

    pais_origen = forms.ModelChoiceField(queryset=models.Pais.objects.all())

    def clean_id(self):
        id = self.cleaned_data['id']
        if models.Usuario.objects.filter(id=id).exists():
            raise forms.ValidationError("Este ID de usuario ya está registrado.")
        return id

class Noticia_Form(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = ["titulo", 
                  "contenido", 
                  "categoria",
                  "autor"]

    categoria = forms.ModelChoiceField(queryset=models.Categoria.objects.all())

class NoticiaBuscarFormulario(forms.Form):
    titulo = forms.CharField(label="Título de la Noticia", max_length=100, required=False)

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        return titulo


class UsuarioBuscarFormulario(forms.Form):
    usuario = forms.CharField(label="Consulta de Usuario", max_length=100, required=False)

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        return usuario