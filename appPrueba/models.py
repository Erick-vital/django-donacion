from django.db import models

# Create your models here.

class ModeloTareas(models.Model):
    tarea = models.CharField(max_length=20)

    def __str__(self):
        return self.tarea

class CheckboxModel(models.Model):
    relacion = models.OneToOneField(ModeloTareas,
    on_delete=models.CASCADE,
    )
    checkbox = models.BooleanField(default=False)
