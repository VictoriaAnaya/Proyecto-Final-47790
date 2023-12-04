from django.shortcuts import render

def inicio_view(request):
    return render(request, 'AppCoder/inicio.html')

def usuarios_view(request):
    return render(request, 'AppCoder/base.html')

def about_view(request):
    return render(request, 'AppCoder/about.html')

def foros_view(request):
    return render(request, 'AppCoder/foros.html')

def noticias_view(request):
    return render(request, 'AppCoder/noticias.html')