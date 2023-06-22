from django.contrib import admin
from .models import concesionesMaritimas

# Se define una clase concesionesMaritimasAdmin que hereda de admin.ModelAdmin
# Esta clase se utiliza para personalizar la interfaz de administración del modelo concesionesMaritimas
class concesionesMaritimasAdmin(admin.ModelAdmin):
    list_display = ('numero_id','numero_concesion', 'tipo_de_concesion','comuna','lugar','numero_rs_ds', 'tipo_tramite', 'concersionario', 'tipo_vigencia')
    list_filter = ('tipo_vigencia', 'tipo_tramite') # Filtros que se mostraran en la barra lateral
    search_fields = ('numero_concesion','tipo_de_concesion') # Campos por los que se podran realizar busquedas

# Se registra la clase concesionesMaritimasAdmin como administrador del modelo concesionesMaritimas
# Esto permite visualizar y administrar los objetos concesionesMaritimas en la interfaz de administracion
admin.site.register(concesionesMaritimas, concesionesMaritimasAdmin)
