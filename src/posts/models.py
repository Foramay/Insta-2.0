from django.db import models
from usuarios.models import Usuario

class Posts(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField()


    class Meta:
        #Acá le damos un nombre personalizado a la tabla
        db_table = 'posts'