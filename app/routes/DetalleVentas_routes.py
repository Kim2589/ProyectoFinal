from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.DetalleVentas import DetalleVentas
from app import db

bp = Blueprint('DetalleVentas', __name__)

@bp.route('/DetalleVentas')
def index():
    data = DetalleVentas.query.all()
 
    return render_template('DetalleVentas/index.html', data=data)

@bp.route('/DetalleVentas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cantidadDetalleVentas = request.form['cantidadDetalleVentas']
        subTotalDetalleVentas = request.form['subTotalDetalleVentas']
        idVentas = request.form['idVentas']
        idProductos = request.form['idProductos']
        

        new_DetalleVentas = DetalleVentas(cantidadDetalleVentas=cantidadDetalleVentas, subTotalDetalleVentas=subTotalDetalleVentas, idVentas=idVentas, idProductos=idProductos)
        db.session.add(new_DetalleVentas)
        db.session.commit()
        
        return redirect(url_for('DetalleVentas.index'))

    return render_template('DetalleVentas/add.html')

@bp.route('/DetalleVentas/edit/<int:idDetalleVentas>', methods=['GET', 'POST'])
def edit(idDetalleVentas):
    detalle_venta = DetalleVentas.query.get_or_404(idDetalleVentas)

    if request.method == 'POST':
        detalle_venta.cantidadDetalleVentas = request.form['cantidadDetalleVentas']
        detalle_venta.subTotalDetalleVentas = request.form['subTotalDetalleVentas']
        detalle_venta.idVentas = request.form['idVentas']
        detalle_venta.idProductos = request.form['idProductos']
     

        db.session.commit()
        return redirect(url_for('DetalleVentas.index'))

    return render_template('DetalleVentas/edit.html', detalle_venta=detalle_venta)
    

@bp.route('/DetalleVentas/delete/<int:idDetalleVentas>')
def delete(idDetalleVentas):
    detalle_venta = DetalleVentas.query.get_or_404(idDetalleVentas)
    
    db.session.delete(detalle_venta)
    db.session.commit()

    return redirect(url_for('DetalleVentas.index'))
