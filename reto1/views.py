from django.shortcuts import render
from django.http import HttpResponse
from requests import get
from requests import exceptions



def get_jurisprudencias(request):
    url = 'https://www.buscadorambiental.cl/buscador/#/jurisprudencias'
    try:
        response =get(url)
        return HttpResponse(response)
        if response.status_code == 200:
            return HttpResponse(response.text)
        else:
            return HttpResponse(f'Error en la petición. Código de estado: {response.status_code}')
    except exceptions.RequestException as e:
        return HttpResponse(f'Error de conexión: {e}')
