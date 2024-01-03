from django.db import models
import uuid

class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    tiempo = models.DateTimeField(auto_now_add=True)
    actualizar = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True