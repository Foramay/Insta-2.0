from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Canal, CanalMensaje, CanalUsuario
from django.http import HttpResponse, Http404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class DetailMs(LoginRequiredMixin, DetailView):
    template_name = 'dm/canal_detail.html'
    def get_object(self, *args, **kwargs):
        username = self.kwargs.get('username')
        mi_username = self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)
        if canal == None:
            raise Http404
        return canal
 





def mensajes_privados(request, username, *args, **kwargs):

    if not request.user.is_authenticated:
        return HttpResponse("Prohibido")
    
    mi_username = request.user.username
    canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

    if created:
        print("Si, fue creado")


    Usuarios_Canal = canal.canalusuario_set.all().values('usuario__username')
    print(Usuarios_Canal)

    mensaje_canal = canal.canalmensaje_set.all()
    print(mensaje_canal.values('texto'))
    return HttpResponse(f'Nuestro canal - {canal.id}')
