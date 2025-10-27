from django.urls import path
from associados.views import index
urlpatterns = [
    path('index',index, name='index'),

]