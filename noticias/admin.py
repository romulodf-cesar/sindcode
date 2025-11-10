from django.contrib import admin

from noticias.models import Noticia
from noticias.models import Categoria
from noticias.models import Autor


admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Noticia)
