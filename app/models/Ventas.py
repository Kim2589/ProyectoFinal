from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Ventas(db.Model):
    __tablename__ ='venta'
    idVentas = db.Column(db.Integer, primary_key=True)
    fechaVentas = db.Column(db.Date, nullable=False, default=func.now())
    cantidadVentas = db.Column(db.Integer, nullable=False)
    idUsuarios = db.Column(db.Integer, db.ForeignKey('usuario.idUsuarios'))
    idEmpleados = db.Column(db.Integer, db.ForeignKey('empleado.idEmpleados'))
    total = db.Column(db.Integer, nullable=False)   
    usuarios = db.relationship("Usuarios", back_populates="ventas")
    empleados = db.relationship("Empleados", back_populates="ventas")

