from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255, null=True, blank=True)



    def following(self):
        user_ids = Relationship.objects.filter(from_user=self).values_list('to_user_id', flat=True)

        return Usuario.objects.filter(id__in=user_ids)
    
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self)\
        .values_list('from_user_id', flat=True)

        return Usuario.objects.filter(id__in=user_ids)

    class Meta:
        #Acá le damos un nombre personalizado a la tabla
        db_table = 'usuarios'


class Relationship(models.Model):
    from_user = models.ForeignKey(Usuario, related_name='relationship', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Usuario, related_name='related_to', on_delete=models.CASCADE)