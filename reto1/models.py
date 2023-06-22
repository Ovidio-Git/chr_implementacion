from django.db import models

# Creacion modelos para guardar las jurisprudencias con sus valores asociados 
# y se realacionan estas para que se puedan unir cuando se consulten los datos
class Jurisprudencias(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_causa = models.CharField(max_length=1)
    rol = models.CharField(max_length=200)
    caratula = models.CharField(max_length=700)
    nombre_proyecto = models.CharField(max_length=700)
    fecha_sentencia = models.DateField()
    descriptores = models.TextField()
    link_sentencia = models.CharField(max_length=700)
    url_sentencia = models.CharField(max_length=700)
    activo = models.BooleanField()
    tribunal = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    relacionada = models.CharField(max_length=100)
    visitas = models.IntegerField()

    def __str__(self):
        return f"{self.tipo}-{self.rol}"
    
class valoresJudisprudencias(models.Model):
    id = models.IntegerField(primary_key=True)
    idParametro = models.IntegerField()
    idItemlista = models.IntegerField(null=True)
    valor = models.CharField(max_length=1500, null=True)
    parametro = models.CharField(max_length=700)
    item = models.CharField(max_length=700, null=True)
    jurisprudencia = models.ForeignKey(Jurisprudencias, on_delete=models.CASCADE, related_name='valores')

    def __str__(self):
        return f"{self.parametro}: {self.valor}"