import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'uploadfile' not in request.files:
        return 'No se ha seleccionado ningún archivo'
    
    file = request.files['uploadfile']

    if file.filename == '':
        return 'No se ha seleccionado ningún archivo'

    # Leer el contenido del archivo
    file_contents = file.read()
    return 'Archivo recibido exitosamente'

if __name__ == '__main__':
    app.run(debug=True, port=4000)
