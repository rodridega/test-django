from django.http import HttpResponse
import datetime

def getAll(request):
    return HttpResponse("Hola mundo")


def fecha(request):
    fechaActual = datetime.datetime.now()

    return HttpResponse(fechaActual)

def edad(request, ano):

    edadActual = 32
    periodo = ano - 2022
    edadFut = edadActual + periodo

    return HttpResponse(edadFut)