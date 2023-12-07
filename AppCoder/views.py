from django.shortcuts import render, redirect
from . import models
from datetime import date
from . import forms

def inicio_view(request):
    return render(request, 'AppCoder/index.html')

def usuarios_view(request):
    usuarios = models.Usuario.objects.all()
    context = {"usuarios": usuarios }
    return render(request, 'AppCoder/usuarios.html', context)

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


def card_view(request):
    contenido = [
        {"titulo": "Autores", "descripcion": "Conocé las últimas publicaciones y noticias de tus autores favoritos", "url": "usuarios"},
        {"titulo": "Noticias", "descripcion": "Mantente al día con las últimas noticias y eventos que están marcando tendencia", "url": "noticias"},
        {"titulo": "Inversiones", "descripcion": "Descubrí oportunidades de inversión y consejos financieros para tu crecimiento.", "url": "foros"},
    ]

    context = {
        'contenido': contenido,
    }

    return render(request, 'AppCoder/card.html', context)


def crear_usuarios(request):
    usuarios = models.Usuario.objects.all()
    if request.method == "POST":
        form = forms.Usuario_Form(request.POST)
        try:
         if form.is_valid():
            form.save()
            return redirect("AppCoder:usuarios")
        except: 
         forms.add_error(None, "Este usuario ya está registrado.")
    else:
        form = forms.Usuario_Form()
    return render(request, "AppCoder/crear_usuarios.html", {"form": forms.Usuario_Form()})
        
    
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
