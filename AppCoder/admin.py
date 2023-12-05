from django.contrib import admin

from .models import Pais, Usuario, Categoria, Noticia, Comentario

admin.site.register(Pais)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Comentario)

