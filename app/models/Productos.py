from app import db

class Productos(db.Model):
    __tablename__ = 'producto'
    idProductos = db.Column(db.Integer, primary_key=True)
    nombreProductos = db.Column(db.String(255), nullable=False)
    descripcionProductos = db.Column(db.String(255), nullable=False)
    precioProductos = db.Column(db.Integer, nullable=False)
    fechaLoteProductos = db.Column(db.Date, nullable=False)
    nombreImagen = db.Column(db.String(255), nullable=False, default="sinfoto.jpg")