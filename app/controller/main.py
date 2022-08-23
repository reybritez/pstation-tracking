from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html', title='Sisepuede paa') # Ruta principal de inicio

#Aca se pueden crear más rutas y sin la estructura orginal que tiene ésta app que es modular
#Pero se recomienda utilizar esta configuración para que el header y el footer de toda la app sea consistente en todo el sitio.