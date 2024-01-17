from django.urls import path
from .views import (
    mensajes_privados,
    DetailMs
    )


app_name = 'dm'


urlpatterns = [
    path('dm/<str:username>', mensajes_privados),
    path('ms/<str:username>', DetailMs.as_view(), name='detailms')
]
