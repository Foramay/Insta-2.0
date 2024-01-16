from django.urls import path
from .views import (
    mensajes_privados
    )


app_name = 'dm'


urlpatterns = [
    path('dm/<str:username>', mensajes_privados)
    #Includes de usu
]
