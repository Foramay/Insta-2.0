from django.db import models
from usuarios.models import Usuario

class Posts(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='image_post', null=True, blank=True)
    descripcion = models.TextField()


    class Meta:
        #Acá le damos un nombre personalizado a la tabla
        db_table = 'posts'