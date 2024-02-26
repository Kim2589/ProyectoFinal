from app import db


class DetalleCompras(db.Model):
    __tablename__ ='detalle_compra'
    idDetalleCompras = db.Column(db.Integer, primary_key=True)
    cantidadDetalles = db.Column(db.Integer, nullable=False)
    subTotalDetalles = db.Column(db.Integer, nullable=False)
    idProductos = db.Column(db.Integer, db.ForeignKey('producto.idProductos'))
    idCompras = db.Column(db.Integer, db.ForeignKey('compra.idCompras'))


