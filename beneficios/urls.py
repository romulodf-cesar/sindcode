from django.urls import path
from beneficios.views import beneficios
urlpatterns = [
    path('beneficios',beneficios, name='beneficios'),


]
