from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Ventas import Ventas
from app.routes.Carrito_routes import carrito_ventas
from app import db

bp = Blueprint('Ventas', __name__)

@bp.route('/Ventas')
def index():
    data = Ventas.query.all()
    # Ventas_list = [Ventas.to_dict() for book in data]
    # return jsonify(Ventas_list)
    return render_template('Ventas/index.html', data=data)

@bp.route('/Ventas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaVentas = request.form['fechaVentas']
        cantidadVentas = request.form['cantidadVentas']
        idUsuarios = request.form['idUsuarios']
        idEmpleados = request.form['idEmpleados']

        new_Ventas = Ventas(fechaVentas=fechaVentas, cantidadVentas=cantidadVentas, idusuarios=idUsuarios, idEmpleados=idEmpleados)
        db.session.add(new_Ventas)
        db.session.commit()
        
        return redirect(url_for('Ventas.index'))

@bp.route('/Ventas/edit/<int:idVentas>', methods=['GET', 'POST'])
def edit(idVentas):
    venta = Ventas.query.get_or_404(idVentas)

    if request.method == 'POST':
        venta.fechaVentas = request.form['fechaVentas']
        venta.cantidadVentas = request.form['cantidadVentas']
        venta.idUsuarios = request.form['idUsuarios']
        venta.idEmpleados = request.form['idEmpleados']

        db.session.commit()
        return redirect(url_for('Ventas.index'))

    return render_template('Ventas/edit.html', venta=venta)
    

@bp.route('/Ventas/delete/<int:idVentas>')
def delete(idVentas):
    ventas = Ventas.query.get_or_404(idVentas)
    
    db.session.delete(ventas)
    db.session.commit()

    return redirect(url_for('Ventas.index'))
