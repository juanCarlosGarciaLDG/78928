from flask import flask 
from rutas import rutas_bp

app = Flask(__name__)
app.register_blueprint(rutas_bp)

@app.route('/')
def inicio():
    return 'Pagina de Inicio'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)