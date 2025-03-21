from flask import Blueprint 
rutas_bp = Blueprint('rutas', __name__, url_prefix='/api/v1')

@rutas_bp.route('/ruta1')
def ruta1():
    return 'Esta es la ruta 1'

@rutas_bp.route('/ruta2')
def ruta2():
    return 'esta es la ruta2'