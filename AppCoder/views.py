from django.shortcuts import render, redirect
from . import models
from datetime import date
from . import forms

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
            return redirect("AppCoder:usuarios")

    context = {
        'form_registro': form_registro,
    }
    return render(request, 'AppCoder/crear_usuarios.html', context)

def buscar_usuario_view(request):
    usuarios = models.Usuario.objects.all()
    usuario_encontrado = None
    form_busqueda = forms.UsuarioBuscarFormulario()

    if request.method == 'POST' and 'buscar_usuario' in request.POST:
        form_busqueda = forms.UsuarioBuscarFormulario(request.POST)
        if form_busqueda.is_valid():
            usuario_buscado = form_busqueda.cleaned_data['usuario']
            usuarios_encontrados = models.Usuario.objects.filter(nombre__icontains=usuario_buscado)

            if usuarios_encontrados:
                usuario_encontrado = usuarios_encontrados.first()

    context = {
        'form_busqueda': form_busqueda,
        'usuarios': usuarios,
        'usuario_encontrado': usuario_encontrado,
    }
    return render(request, 'AppCoder/buscar_usuarios.html', context)

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
    if request.method == "GET":
        form = forms.NoticiaBuscarFormulario()
        return render(
            request,
            "AppCoder/buscar_noticia.html", 
            context={"form": form}
        )
    else:
        formulario = forms.NoticiaBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            noticias_filtradas = models.Noticia.objects.filter(titulo__icontains=informacion["titulo"])
            contexto = {"noticias": noticias_filtradas}
            return render(request, "App/noticias.html", contexto)

    
def crear_noticia(request):
    noticias = models.Noticia.objects.all()
    if request.method == "POST":
        form = forms.Noticia_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AppCoder:crear_noticia")
    else:
        form = forms.Noticia_Form()
    return render(request, "AppCoder/crear_noticia.html", {"form": forms.Noticia_Form()})



        

