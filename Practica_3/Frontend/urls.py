from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cargarxml', views.cargarxml, name='cargarxml'),
    path('subir_archivo', views.subir_archivo, name='subirxml')
]