from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludos(request):  # Primera vista
    doc_externo = open(
        "D:/Desktop/Prueba/DashboardDjango/DashboardDjangoSoftware/DashboardDjangoSoftware/templates/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Adios mundo")


def ObtenerFecha(request):
    fecha_actual = datetime.datetime.utcnow()

    documento = "<html><body><h1> Fecha y hora actuales %s </h1></body></html>" % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, edad, year):
    #edadActual = 18
    periodo = year-2020
    edadFutura = edad+periodo
    documento = "<html><body><h2>En el año %s tendras %s años" % (
        year, edadFutura)
    return HttpResponse(documento)
