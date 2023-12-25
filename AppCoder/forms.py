from django import forms

from . import models

class Usuario_Form(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'

    pais_origen = forms.ModelChoiceField(queryset=models.Pais.objects.all())

    def clean_id(self):
        ID = self.cleaned_data['ID']
        if models.Usuario.objects.filter(id=id).exists():
            raise forms.ValidationError("Este ID de usuario ya está registrado.")
        return ID

class Noticia_Form(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = ["numero",
                  "titulo", 
                  "contenido", 
                  "categoria",
                  "autor"]

    categoria = forms.ModelChoiceField(queryset=models.Categoria.objects.all())

class NoticiaBuscarFormulario(forms.Form):
    autor = forms.CharField(label='Autor', max_length=100, required=False)

    def clean_numero(self):
        autor = self.cleaned_data['autor']
        return autor

class NoticiaEditarFormulario(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = ['titulo', 'contenido']

class UsuarioBuscarFormulario(forms.Form):
    usuario = forms.CharField(label="Consulta de Usuario", max_length=100, required=False)

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        return usuario
    


#----------------------------------------- registro -------------------------------------------------------------

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


class UserCreationFormulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["password1", "password2", "username", "email"]
        help_texts = {k: "" for k in fields}

class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido", widget=forms.PasswordInput)
    password = None

    class Meta:
        model = UserModel
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}


class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = models.Avatar
        fields = ["imagen"]