from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Ruta principal (El sitio que se ve "normal")
@app.route('/')
def index():
    return render_template('index.html')

# SIMULACIÓN DE VULNERABILIDAD: Mala configuración de listado de directorios
@app.route('/static/uploads/')
def list_uploads():
    upload_dir = os.path.join(app.root_path, 'static', 'uploads')
    files = os.listdir(upload_dir)
    
    html = "<h1>Index of /static/uploads/</h1><hr><ul>"
    for file in files:
        html += f'<li><a href="/static/uploads/{file}">{file}</a></li>'
    html += "</ul><hr>"
    return html

# Ruta para descargar los archivos
@app.route('/static/uploads/<filename>')
def download_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'uploads'), filename)

if __name__ == '__main__':
    # Escucha en todas las interfaces para que tus compañeros puedan acceder
    app.run(host='0.0.0.0', port=5000, debug=True)