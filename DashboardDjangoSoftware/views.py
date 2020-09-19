from django.http import HttpResponse
import datetime


def saludos(request):  # Primera vista
    return HttpResponse("Hola mundo")


def despedida(request):
    return HttpResponse("Adios mundo")


def ObtenerFecha(request):
    fecha_actual = datetime.datetime.utcnow()

    documento = "<html><body><h1> Fecha y hora actuales %s </h1></body></html>" % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, year):
    edadActual = 18
    periodo = year-2020
