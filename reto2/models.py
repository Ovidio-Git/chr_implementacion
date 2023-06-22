from django.db import models
from django.utils import timezone


# Creacion modelo para guardar las conseciones maritimas
class concesionesMaritimas(models.Model):
    numero_id = models.IntegerField(primary_key=True)
    numero_concesion = models.IntegerField()
    tipo_de_concesion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    lugar = models.CharField(max_length=400)
    numero_rs_ds = models.CharField(max_length=50)
    tipo_tramite = models.CharField(max_length=200)
    concersionario = models.CharField(max_length=400)
    tipo_vigencia = models.CharField(max_length=200)
    fecha_creacion_dato = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.nombre}"