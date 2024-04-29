from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    return render (request, 'Home.html')

def cargarxml(request):
    return render (request, 'Cargarxml.html')

def subir_archivo(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('uploadfile')
        if upload_file:
            # Envía el archivo al backend Flask solo si hay un archivo adjunto en la solicitud
            url = 'http://127.0.0.1:4000/upload'
            files = {'uploadfile': upload_file}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                # El archivo se cargó exitosamente en el backend Flask
                mensaje = 'Archivo cargado exitosamente'
            else:
                # Ocurrió un error al cargar el archivo en el backend Flask
                mensaje = 'Error al cargar el archivo'
        else:
            # No se adjuntó ningún archivo en la solicitud POST
            mensaje = 'No se ha seleccionado ningún archivo'
    else:
        # La solicitud no es POST
        mensaje = 'La solicitud debe ser de tipo POST'
    
    # Renderiza la plantilla con el mensaje
    return render(request, 'mensaje.html', {'mensaje': mensaje})

def mostrar_archivo(request):
    contenido_respons = requests.get('http://127.0.0.1:4000/cargardatos')
    contenido_archivo = contenido_respons.text

    return render(request, 'Datosprocesados.html', {'contenido_archivo': contenido_archivo})

def borrar_datos_backend(request):
    url = 'http://127.0.0.1:4000/borrardatos'
    response = requests.delete(url)
    if response.status_code == 200:
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=500)

def datosestudiante(request):
    return render (request, 'Datos.html')