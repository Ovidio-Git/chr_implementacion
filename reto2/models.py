from django.db import models

# Create your models here.
class concesionesMaritimas(models.Model):
    numero_id = models.IntegerField(primary_key=True)
    numero_concesion = models.IntegerField()
    tipo_de_concesion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    lugar = models.CharField(max_length=50)
    numero_rs_ds = models.CharField(max_length=50)
    tipo_tramite = models.CharField(max_length=100)
    concersionario = models.CharField(max_length=100)
    tipo_vigencia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.nombre}"