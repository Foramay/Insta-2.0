from django.shortcuts import render
from .models import Canal, CanalMensaje, CanalUsuario
from django.http import HttpResponse

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
