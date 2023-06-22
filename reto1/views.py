from django.shortcuts import render
from django.http import HttpResponse
from requests import exceptions
from requests import post
from json import dumps
from .models import Jurisprudencias
from .models import valoresJudisprudencias
from datetime import datetime



def guardar_informacion_postgres(data_para_guardar)->None:
    """
    Guarda la informacion de las jusrisprudencias en la base de datos PostgreSQL.
    
    Args:
        data_para_guardar: Lista de datos a guardar en la base de datos.
    Returns:
        None
    """  
    
    # Iterar sobre la lista de jurisprudencias
    for data in data_para_guardar:
        # Dar formato a fecha sentencia para la base de datos 
        fecha_sentencia = data["fechaSentencia"]
        fecha_sentencia_obj = datetime.strptime(fecha_sentencia, "%d-%m-%Y")
        fecha_sentencia_formateada = fecha_sentencia_obj.strftime("%Y-%m-%d")
        # Crear instancia del modelo Jurisprudencia
        instancia_jurisprudencia = Jurisprudencias(
            id=data["id"],
            tipo_causa=data["tipoCausa"],
            rol=data["rol"],
            caratula=data["caratula"],
            nombre_proyecto=data["nombreProyecto"],
            fecha_sentencia=fecha_sentencia_formateada,
            descriptores=data["descriptores"],
            link_sentencia=data["linkSentencia"],
            url_sentencia=data["urlSentencia"],
            activo=data["activo"],
            tribunal=data["tribunal"],
            tipo=data["tipo"],
            relacionada=data["relacionada"],
            visitas=data["visitas"]
        )
        instancia_jurisprudencia.save()  # Guardar la informacion en la base de datos

        # Crear instancias de ValorJurisprudencia
        valores = data["valores"]
        for valor in valores:
            instancia_valor_jurisprudencia = valoresJudisprudencias(
                id=valor["id"],
                idParametro=valor["idParametro"],
                idItemlista=valor["idItemlista"],
                valor=valor["valor"],
                parametro=valor["parametro"],
                item=valor["item"],
                jurisprudencia=instancia_jurisprudencia  # Establecer relacion con la Jurisprudencia correspondiente
            )
            instancia_valor_jurisprudencia.save() # Guardar la informacion de los valores realcionados en la base de datos



def get_jurisprudencias(request):
    # URL de la pagina para obtener la lista de jurisprudencias
    url = 'https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list'
    # Encabezados de la solicitud POST
    headers = { "Content-Type": "application/json"}
    # Cuerpo de la solicitud POST con los parametros de la consulta
    peticion_body = {
            "page":1,# Numero de pagina a solicitar
            "pageSize":10,# Tamaño de pagina (cantidad de jurisprudencias por pagina)
            "orden":"nuevo"# Orden de la lista (en este caso, por fecha mas reciente)
        }
    try:
        # Realizar la solicitud POST a la URL con los encabezados y el cuerpo
        response = post(url,data=dumps(peticion_body), headers=headers)
        # Verificar el codigo de estado de la respuesta
        if response.status_code == 200:
            # Obtener la respuesta en formato JSON
            respuesta_post_jurisprudencias = response.json()
            # Extraer la lista de jurisprudencias de la respuesta
            listado_jurisprudencias = respuesta_post_jurisprudencias["jurisprudencias"]
            # Guardar la informacion de las jurisprudencias en la base de datos
            guardar_informacion_postgres(listado_jurisprudencias)
            # Devolver la lista de jurisprudencias como respuesta HTTP
            return HttpResponse(listado_jurisprudencias)
        else:
            # Devolver un mensaje de error si la respuesta tiene un codigo de estado distinto de 200
            return HttpResponse(f'Error en la peticion. Codigo de estado: {response.status_code}')
    except exceptions.RequestException as e:
        return HttpResponse(f'Error de conexion: {e}')
