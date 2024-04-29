from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cargarxml', views.cargarxml, name='cargarxml'),
    path('subir_archivo', views.subir_archivo, name='subirxml'),
    path('mostrar_archivo', views.mostrar_archivo, name='mostrar_archivo'),
    path('borrar_datos_backend', views.borrar_datos_backend, name='borrar_datos_backend'),
    path('datosestudiante', views.datosestudiante, name='datosestudiante' )
]