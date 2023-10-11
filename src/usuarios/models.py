from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255, null=True, blank=True)



    class Meta:
        #Acá le damos un nombre personalizado a la tabla
        db_table = 'usuarios'