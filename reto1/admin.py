from django.contrib import admin
from .models import Jurisprudencias
from .models import valoresJudisprudencias

# Se define una clase ValoresJurisprudenciasInline que hereda de admin.TabularInline
# Se relaciona con el modelo valoresJudisprudencias para tener los datos completos
class ValoresJurisprudenciasInline(admin.TabularInline):
    model = valoresJudisprudencias  # Se especifica el modelo con el que se relaciona


# Se define una clase JurisprudenciasAdmin que hereda de admin.ModelAdmin
# Esta clase se utiliza para personalizar la interfaz de administracion del modelo Jurisprudencias
class JurisprudenciasAdmin(admin.ModelAdmin):
    list_display = ('rol', 'caratula', 'fecha_sentencia') # Campos que se mostraran en la vista
    list_filter = ('tipo_causa', 'tribunal') # Filtros que se mostrarán en la barra lateral
    search_fields = ('rol', 'caratula') # Campos por los que se podrán realizar búsquedas
    inlines = [ValoresJurisprudenciasInline]

# Se registra la clase JurisprudenciasAdmin como administrador del modelo Jurisprudencias
# Esto permite visualizar y administrar los objetos Jurisprudencias en la interfaz de administración
admin.site.register(Jurisprudencias, JurisprudenciasAdmin)