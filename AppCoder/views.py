from django.shortcuts import render, redirect, get_object_or_404
from . import models
from datetime import date
from . import forms
from . models import Usuario
from django.contrib.auth.decorators import login_required
from .forms import UserEditionFormulario 
from .models import Avatar

def inicio_view(request):
    return render(request, 'AppCoder/index.html')

def crear_usuario_view(request):
    form_registro = forms.Usuario_Form()

    if request.method == 'POST' and 'registrar_usuario' in request.POST:
        form_registro = forms.Usuario_Form(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            return redirect("AppCoder:detalle_usuarios")

    context = {
        'form_registro': form_registro,
    }
    return render(request, 'AppCoder/crear_usuarios.html', context)

def buscar_usuario_view(request):
    usuarios_encontrados = None
    if request.method == 'POST':
        form = forms.UsuarioBuscarFormulario(request.POST)
        if form.is_valid():
            email_buscado = form.cleaned_data['usuario']
            usuarios_encontrados = Usuario.objects.filter(email__icontains=email_buscado)

    context = {
        'form': forms.UsuarioBuscarFormulario(),
        'usuarios_encontrados': usuarios_encontrados,
    }
    return render(request, 'AppCoder/buscar_usuarios.html', context)


def detalle_usuario_view(request, ID):
    usuario = get_object_or_404(Usuario, id=ID)
    context = {'usuario': usuario}
    return render(request, 'AppCoder/detalle_usuario.html', context)

def about_view(request):
    return render(request, 'AppCoder/about.html')

def foros_view(request):
    return render(request, 'AppCoder/foros.html')

def noticias_view(request):
    noticias = models.Noticia.objects.all()
    categorias = models.Categoria.objects.all()
    context = {"noticias": noticias, "categorias": categorias}
    return render(request, 'AppCoder/noticias.html', context)

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(models.Noticia, pk=noticia_id)
    return render(request, 'AppCoder/detalle_noticias.html', {'noticia': noticia})

def buscar_noticia_view(request):
    noticia_encontrada = None
    form_busqueda = forms.NoticiaBuscarFormulario()

    if request.method == 'POST' and 'buscar_noticia' in request.POST:
        form_busqueda = forms.NoticiaBuscarFormulario(request.POST)
        if form_busqueda.is_valid():
            autor_buscado = form_busqueda.cleaned_data['autor']
            noticias_encontradas = models.Noticia.objects.filter(autor__icontains=autor_buscado)

            if noticias_encontradas.exists():
                noticia_encontrada = noticias_encontradas.first()
                return redirect('AppCoder:detalle_noticia', noticia_id=noticia_encontrada.id)

    context = {
        'form_busqueda': form_busqueda,
        'noticia_encontrada': noticia_encontrada,
    }
    return render(request, 'AppCoder/buscar_noticias.html', context)

    
def crear_noticia(request):
    noticias = models.Noticia.objects.all()
    if request.method == "POST":
        form = forms.Noticia_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AppCoder:noticias")
    else:
        form = forms.Noticia_Form()
    return render(request, "AppCoder/crear_noticia.html", {"form": forms.Noticia_Form()})



def eliminar_noticia_view(request, id_noticia):
    noticia = get_object_or_404(models.Noticia, id_noticia=id_noticia)
    if request.method == 'POST':
        noticia.delete()
        return redirect('AppCoder:buscar_noticia')

    return render(request, 'AppCoder/eliminar_noticia.html', {'noticia': noticia})


def editar_noticia_view(request, id_noticia):
    noticia = get_object_or_404(models.Noticia, id_noticia=id_noticia)
    form = forms.NoticiaEditarFormulario(instance=noticia)

    if request.method == 'POST':
        form = forms.NoticiaEditarFormulario(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:buscar_noticia')

    return render(request, 'AppCoder/editar_noticia.html', {'form': form, 'noticia': noticia})
        
#---------------------------CRUD-------------------------------------------------------------

@login_required
def usuarios_view(request):
    if request.method == "GET":
        return render(
            request,
            "AppCoder/usuarios.html",
            {"form": forms.Usuario_Form()}
        )
    else:
        formulario = forms.Usuario_Form(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Usuario(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                intereses=informacion["intereses"],
                pais_origen=informacion["país de origen"],
                nacimiento=informacion["fecha de nacimiento"]
            )
            modelo.save()
        return render(
            request,
            "AppCoder/index.html",
        )

@login_required
def obtener_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'AppCoder/usuarios_lista.html', {'usuarios': usuarios})


@login_required
def eliminar_usuario_view(request, ID):
    usuario = get_object_or_404(Usuario, id=ID)

    if request.method == 'POST':
        usuario.delete()
        return redirect('AppCoder:buscar_usuarios')

    context = {'usuario': usuario}
    return render(request, 'AppCoder/eliminar_usuario.html', context)


@login_required
def editar_usuario_view(request, id):
    usuario = Usuario.objects.filter(Usuario, ID=id).first()
    if request.method == "GET":
        formulario = forms.Usuario_Form(
            initial={
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "email": usuario.email,
                "intereses": usuario.intereses,
                "fecha de nacimiento": usuario.nacimiento,
                "pais de origen": usuario.pais_origen,
            })
        return render(request, 'AppCoder/editar_usuario.html', {'forms': forms, 'usuario': usuario})
    else:
        formulario = forms.Usuario_Form(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.nombre=informacion["nombre"]
            usuario.apellido=informacion["apellido"]
            usuario.email=informacion["email"]
            usuario.intereses=informacion["intereses"]
            usuario.nacimiento=informacion["fecha de nacimiento"]
            usuario.pais_origen=informacion["pais de origen"]
            usuario.save()
        return obtener_usuarios(request)

#------------------------------------------------------------------------------------------#
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    template_name = "AppCoder/cbv_usuario_create.html"
    success_url = reverse_lazy("AppCoder:usuarios_lista")
    form_class = forms.UserCreationForm
   
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    context_object_name = "usuarios"
    template_name = 'AppCoder/cbv_usuario_list.html'

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'AppCoder/cbv_usuario_detail.html'

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'AppCoder/cbv_usuario_update.html'
    success_url = reverse_lazy("AppCoder:usuarios_lista")
    form_class = forms.UserEditionFormulario

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'AppCoder/cbv_usuario_delete.html'
    success_url = reverse_lazy('usuarios_lista')


    #-----------------------------------------------------------------------------------------------#
    
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/index.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)

            if modelo is not None:
                login(request, modelo)

                # Obtener la URL del avatar y almacenarla en la sesión del usuario
                avatar = Avatar.objects.filter(user=modelo).first()
                avatar_url = avatar.imagen.url if avatar is not None else ""
                request.session['avatar_url'] = avatar_url

                return render(
                    request,
                    "AppCoder/index.html",
                    {"mensaje": f"Bienvenido {modelo.username}"}
                )
            else:
                return render(
                    request,
                    "AppCoder/login.html",
                    {"form": formulario, "error_message": "Usuario o contraseña incorrectos"}
                )
        else:
            return render(
                request,
                "AppCoder/login.html",
                {"form": formulario}
            )

def logout_view(request):
    pass

from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView


def registro_view(request):
    if request.method == "GET":
        return render(
            request,
            "AppCoder/registro.html",
            {"form": forms.UserCreationFormulario()}
        )
    else:
        formulario = forms.UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "AppCoder/registro.html",
                {"form": formulario}
            )
        

#################### CLASE 24:  Editar perfil #########################################

@login_required
def editar_perfil_view(request):
    usuario = request.user
    avatar = models.Avatar.objects.filter(user=usuario).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""

    if request.method == "GET":
        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,  
            "last_name": usuario.last_name  
        }

        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "AppCoder/editar_perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
        )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])
            usuario.first_name = informacion["nombre"] 
            usuario.last_name = informacion["apellido"]  
            usuario.save()

        return redirect("AppCoder:index")


@login_required
def crear_avatar_view(request):

    usuario = request.user

    if request.method == "GET":
        formulario =forms.UserAvatarFormulario()
        return render(
            request,
            "AppCoder/crear_avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = forms.UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = models.Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect("AppCoder:inicio")