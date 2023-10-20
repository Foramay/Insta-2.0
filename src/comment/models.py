from django.db import models
from usuarios.models import Usuario
from posts.models import Posts

class Comment(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

    class Meta:
        db_table = 'comment'