from app import db
from flask_login import UserMixin


class Usuarios(db.Model, UserMixin):
    __tablename__ = "usuario"
    idUsuarios = db.Column(db.Integer, primary_key=True)
    nombreUsuarios = db.Column(db.String(255), nullable=False)
    direccionUsuarios = db.Column(db.String(255), nullable=False)
    telefonoUsuarios = db.Column(db.String(255), nullable=False)
    correoUsuarios = db.Column(db.String(255), nullable=False)
    contrasenaUsuarios = db.Column(db.String(255), nullable=False)
    ventas = db.relationship("Ventas", back_populates="usuarios")

    def get_id(self):
        return str(self.idUsuarios)
