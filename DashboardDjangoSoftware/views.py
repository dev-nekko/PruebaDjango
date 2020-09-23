from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido


def saludos(request):  # Primera vista
    p1 = Persona("Esto es una prueba ", " si una prueba")
    # name = "Renatto"
    # apellido = "Oyague"
    ahora = datetime.datetime.utcnow()
    temaCurso = ["Plantillas", "modelos",
                 "formularios", "vistas", "despliegue"]
    # doc_externo = open(
    #     "D:/Desktop/Prueba/DashboardDjango/DashboardDjangoSoftware/DashboardDjangoSoftware/templates/index.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    #plantilla = get_template('index.html')
    #ctx = Context({"nombre_persona": p1.name,"apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temaCurso})
    #documento = plantilla.render({"nombre_persona": p1.name, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temaCurso})
    # return HttpResponse(documento)
    return render(request, "index.html", {"nombre_persona": p1.name, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas": temaCurso})


def despedida(request):
    return HttpResponse("Adios mundo")


def ObtenerFecha(request):
    fecha_actual = datetime.datetime.utcnow()

    documento = "<html><body><h1> Fecha y hora actuales %s </h1></body></html>" % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, edad, year):
    # edadActual = 18
    periodo = year-2020
    edadFutura = edad+periodo
    documento = "<html><body><h2>En el año %s tendras %s años" % (
        year, edadFutura)
    return HttpResponse(documento)

# Llamar Templates
def ruta(request):
#   proyecto = obtener_proyecto()
#   rutas = obtener_rutas(proyecto.codPyto)
#   return render(request, 'rutas.html', {'proyecto': proyecto, 'rutas': rutas})
  return render(request, 'rutas.html')

def reconocimiento(request):
  return render(request, 'reconocimiento.html')

# # Realizar consultas
# def get_empleado(): # Funcion de prueba, eliminarlo despues
#   empleado = Empleado.objects.get(dni = '77382771')
#   return empleado

# def obtener_proyecto():
#   proyecto = Proyecto.objects.get(codPyto = 2)
#   return proyecto

# def obtener_rutas(cod):
#   rutas = Ruta.objects.filter(codPyto=cod)
#   return rutas

# def obtener_tramos():
#   tramos = Tramo.objects.all()
#   return tramos