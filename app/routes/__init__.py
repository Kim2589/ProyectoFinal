from flask import Blueprint

bp = Blueprint('main', __name__)


from app.routes import Usuarios_routes, Compras_routes, Carrito_routes, Empleados_routes,  Auth
