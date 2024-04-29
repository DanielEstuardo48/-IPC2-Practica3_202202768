import os
import xml.etree.ElementTree as ET
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    global file_contents
    if 'uploadfile' not in request.files:
        return 'No se ha seleccionado ningún archivo'
    
    file = request.files['uploadfile']

    if file.filename == '':
        return 'No se ha seleccionado ningún archivo'

    # Leer el contenido del archivo
    file_contents = file.read()
    return file_contents

def modificar_xml(xml_str):
    # Parsear el XML
    root = ET.fromstring(xml_str)

    # Crear un nuevo XML con la misma estructura
    nuevo_xml = ET.Element("ingresoAnimales")

    # Diccionario para almacenar la cantidad de cada animal
    cantidad_animales = {'perro': 0, 'gato': 0, 'conejo': 0}

    # Recorrer los elementos del XML original y contar la cantidad de cada tipo de animal
    for child in root:
        if child.tag in cantidad_animales:
            cantidad_animales[child.tag] += 1

    # Agregar elementos al nuevo XML con la cantidad de cada tipo de animal
    for animal, cantidad in cantidad_animales.items():
        animal_element = ET.Element(animal)
        cantidad_element = ET.SubElement(animal_element, "cantidad")
        cantidad_element.text = str(cantidad)
        nuevo_xml.append(animal_element)

    # Convertir el nuevo XML a string
    nuevo_xml_str = ET.tostring(nuevo_xml, encoding="unicode")

    return nuevo_xml_str

@app.route('/cargardatos', methods = ['GET'])
def cargardatos_file():
    global file_contents
    if file_contents is None:
        return 'No hay ningun archivo guardado', 404
    
    nuevo_xml_str = modificar_xml(file_contents)

    return Response(nuevo_xml_str, mimetype='text/xml')

@app.route('/borrardatos', methods=['DELETE'])
def borrar_datos():
    global file_contents
    file_contents = None  # Borra los datos almacenados
    return 'Datos borrados correctamente', 200

if __name__ == '__main__':
    app.run(debug=True, port=4000)
