from flask import (
    Blueprint, make_response, send_from_directory
)

bp = Blueprint('pwa', __name__, url_prefix='')

# Cuando se crea la notificacion para instalar la app en el celular se usa este archivo manifest. Editar la info para el titulo, descripcion y favicon.
@bp.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

#Lo que hace que pueda ser utilizado desde el navegador sin necesidad de tener datos.
@bp.route('/sw.js')
def service_worker():
    response = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response
