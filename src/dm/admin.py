from django.contrib import admin
from .models import CanalMensaje, Canal, CanalUsuario


class CanalMensajeInline(admin.TabularInline):
    model = CanalMensaje
    extra = 1

class CanalUsuarioInline(admin.TabularInline):
    model = CanalUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines = [CanalMensajeInline, CanalUsuarioInline]

    class Meta:
        model = Canal

admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalMensaje)
admin.site.register(CanalUsuario)