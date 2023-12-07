

from django.urls import path
from .views import inicio_view, usuarios_view, foros_view, noticias_view, about_view, crear_usuarios, crear_noticia, card_view

app_name = 'AppCoder'

urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("usuarios/", usuarios_view, name="usuarios"), 
    path('foros/', foros_view, name='foros'),
    path('noticias/', noticias_view, name='noticias'),
    path('about/', about_view, name='about'),
    path('crear_usuarios/',crear_usuarios, name= 'crear usuarios' ),
    path('crear_noticia/', crear_noticia, name='crear_noticia'),
    path('card/', card_view, name='card'),
]
