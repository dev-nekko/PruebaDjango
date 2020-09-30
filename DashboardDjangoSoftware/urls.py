
from django.urls import path
from DashboardDjangoSoftware.views import saludos, despedida, ObtenerFecha, calcularEdad,prueba,test
from . import views

urlpatterns = [
    path('saludos/', saludos),
    path('nosveremos/', despedida),
    path('fecha/', ObtenerFecha),
    path('edades/<int:edad>/<int:year>', calcularEdad),
    path('', views.listaproyectos),
    path('reconocimiento/', views.reconocimiento ),
    path('ruta/', views.ruta),
    path('prueba/', views.prueba),
    path('test/', views.test),
]
