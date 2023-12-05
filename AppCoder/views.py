from django.shortcuts import render

def inicio_view(request):
    return render(request, 'AppCoder/index.html')

def usuarios_view(request):
    return render(request, 'AppCoder/usuarios.html')

def about_view(request):
    return render(request, 'AppCoder/about.html')

def foros_view(request):
    return render(request, 'AppCoder/foros.html')

def noticias_view(request):
    return render(request, 'AppCoder/noticias.html')