from django.shortcuts import render, redirect, get_object_or_404
from . import models
from datetime import date
from . import forms
from django.contrib.auth.decorators import login_required
from . models import Usuario
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

def inicio_view(request):
    return render(request, 'AppCoder/index.html')

def usuarios_view(request, accion=None):
    usuarios = models.Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'AppCoder/usuarios.html', context) 
    
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
    usuario_encontrado = None
    form_busqueda = forms.UsuarioBuscarFormulario()

    if request.method == 'POST':
        form_busqueda = forms.UsuarioBuscarFormulario(request.POST)
        if form_busqueda.is_valid():
            usuario_buscado = form_busqueda.cleaned_data['usuario']
            usuarios_encontrados = Usuario.objects.filter(nombre__icontains=usuario_buscado)

            if usuarios_encontrados.exists():
                usuario_encontrado = usuarios_encontrados.first()
                return redirect('AppCoder:detalle_usuario', usuario_id=usuario_encontrado.id)

    context = {
        'form_busqueda': form_busqueda,
        'usuario_encontrado': usuario_encontrado,
    }
    return render(request, 'AppCoder/buscar_usuarios.html', context)


def detalle_usuario_view(request, ID):
    usuario = get_object_or_404(Usuario, id=ID)
    context = {'usuario': usuario}
    return render(request, 'AppCoder/detalle_usuario.html', context)

def eliminar_usuario_view(request, ID):
    usuario = get_object_or_404(Usuario, id=ID)

    if request.method == 'POST':
        usuario.delete()
        return redirect('AppCoder:buscar_usuarios')

    context = {'usuario': usuario}
    return render(request, 'AppCoder/eliminar_usuario.html', context)


def obtener_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'AppCoder/usuarios_lista.html', {'usuarios': usuarios})


def editar_usuario_view(request, id):
    usuario = get_object_or_404(Usuario, ID=id)

    if request.method == 'POST':
        form = forms.Usuario_Form(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('AppCoder:usuarios_lista')
    else:
        form = forms.Usuario_Form(instance=usuario)

    return render(request, 'AppCoder/editar_usuario.html', {'form': form, 'usuario': usuario})

def about_view(request):
    return render(request, 'AppCoder/about.html')

def foros_view(request):
    return render(request, 'AppCoder/foros.html')

def noticias_view(request):
    noticia = models.Noticia.objects.all()
    categoria = models.Categoria.objects.all()
    context = {"noticias": noticia }
    context = {"categorías": categoria }
    return render(request, 'AppCoder/noticias.html', context)


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
        

#------------------------------------------------------------------------------------------#


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'AppCoder/crear_usuarios.html'
    form_class = forms.Usuario_Form
    success_url = 'AppCoder/usuarios_lista'
   
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'AppCoder/usuarios_lista.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'AppCoder/detalle_usuario.html'

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'AppCoder/editar_usuario.html'
    form_class = forms.Usuario_Form

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'eliminar_usuario.html'
    success_url = reverse_lazy('usuarios_lista')


    #-----------------------------------------------------------------------------------------------#
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
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
            login(request, modelo)

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
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