from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'Auth.login'
    
    
    
    @login_manager.user_loader
    def load_user(idUsuarios):
        from app.models.Usuarios import Usuarios
        return Usuarios.query.get(int(idUsuarios))
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.Empleados import Empleados
        return Empleados.query.get(int(user_id))


    from app.routes import Usuarios_routes, Compras_routes, DetalleCompras_routes, DetalleVentas_routes, Empleados_routes, Productos_routes,Proveedores_routes, Ventas_routes,Productos1_routes, Auth, Carrito_routes
    app.register_blueprint(Usuarios_routes.bp)
    app.register_blueprint(Compras_routes.bp)
    app.register_blueprint(DetalleCompras_routes.bp)
    app.register_blueprint(DetalleVentas_routes.bp)
    app.register_blueprint(Empleados_routes.bp)
    app.register_blueprint(Productos_routes.bp)
    app.register_blueprint(Proveedores_routes.bp)
    app.register_blueprint(Ventas_routes.bp)
    app.register_blueprint(Auth.bp)
    app.register_blueprint(Productos1_routes.bp)
    app.register_blueprint(Carrito_routes.bp) 
    

    return app


  




   
    
    

  

   

  