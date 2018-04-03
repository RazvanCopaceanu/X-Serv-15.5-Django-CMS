from django.shortcuts import render
from django.http import HttpResponse

from .models import Pages

def cms(request, recurso):
    try:
        objeto = Pages.objects.get(id=int(recurso))
    except Pages.DoesNotExist:
        return HttpResponse("404 Page Not Found. En Django admin puedes annadir contenidos")
    response = "El nombre es: " + objeto.nombre + " con la descripcion: " + str(objeto.pagina) 
    return HttpResponse(response)
