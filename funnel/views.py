from django.http import HttpResponse
import datetime

from django.template import Context, Template


class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido


def getAll(request):

    p1 = Persona("Rodrigo", "Deganutti")

    nombre = "Rodrigo"

    doc_externo = open(
        "C:/Users/Rodrigo/Desktop/Proyectos/test-django/funnel/plantillas/template.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    contexto = Context({
        "nombre": p1.nombre, "apellido": p1.apellido
    })

    documento = plt.render(contexto)
    return HttpResponse(documento)


def fecha(request):
    fechaActual = datetime.datetime.now()

    return HttpResponse(fechaActual)


def edad(request, ano):

    edadActual = 32
    periodo = ano - 2022
    edadFut = edadActual + periodo

    return HttpResponse(edadFut)
