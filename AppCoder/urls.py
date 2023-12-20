

from django.urls import path
from .views import inicio_view, usuarios_view, foros_view, noticias_view, about_view, crear_noticia, buscar_noticia_view, crear_usuario_view, buscar_usuario_view, delete_user

app_name = 'AppCoder'

urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("usuarios/", usuarios_view, name="usuarios"), 
    path('foros/', foros_view, name='foros'),
    path('noticias/', noticias_view, name='noticias'),
    path('about/', about_view, name='about'),
    path('crear_noticia/', crear_noticia, name='crear_noticia'),
    path('buscar-noticia/', buscar_noticia_view, name='buscar_noticia'),
    path("usuarios/crear/", crear_usuario_view, name="crear_usuarios"),
    path("usuarios/buscar/", buscar_usuario_view, name="buscar_usuarios"),
    path('usuarios/eliminar/<int:id>/', delete_user, name='eliminar_usuario'),
]