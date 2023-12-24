

from django.urls import path
from .views import inicio_view, usuarios_view, foros_view, noticias_view, about_view, crear_noticia, buscar_noticia_view, crear_usuario_view, buscar_usuario_view, detalle_usuario_view, eliminar_usuario_view, eliminar_noticia_view, obtener_usuarios, editar_usuario_view, registro_view, login_view
from. views import UsuarioCreateView, UsuarioDeleteView, UsuarioListView, UsuarioDetailView, UsuarioUpdateView
from django.contrib.auth.views import LogoutView
app_name = 'AppCoder'

urlpatterns = [
    path("", inicio_view, name="inicio"),
    path("usuarios/", usuarios_view, name="usuarios"), 
    path('foros/', foros_view, name='foros'),
    path('noticias/', noticias_view, name='noticias'),
    path('about/', about_view, name='about'),
    path('crear_noticia/', crear_noticia, name='crear_noticia'),
    path('buscar-noticia/', buscar_noticia_view, name='buscar_noticia'),
    path("usuarios/crear/", UsuarioCreateView.as_view(), name="crear_usuarios"),
    path("usuarios/buscar/", buscar_usuario_view, name="buscar_usuarios"),
    path('usuarios/detalle/<int:pk>/', UsuarioDetailView.as_view(), name='detalle_usuario'),
    path('usuarios/eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='eliminar_usuario'),
    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('usuarios/lista/', UsuarioListView.as_view(), name='usuarios_lista'),
    path('eliminar_noticia/<int:id_noticia>/', eliminar_noticia_view, name='eliminar_noticia'),
   

    ###### LOGIN
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
]

    
