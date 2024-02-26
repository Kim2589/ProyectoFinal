from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Productos import Productos
from app.routes.Carrito_routes import carrito_ventas
from app import db
from flask_login import login_required



bp = Blueprint('Productos1', __name__)

@bp.route('/Productos1')
def index():
    data = Productos.query.all()
    # Productos_list = [Productos.to_dict() for book in data]
    # return jsonify(Productos_list)
    return render_template('Productos1/index.html', data=data,t=carrito_ventas.tamañoD())

@bp.route('/Productos/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nombreProductos = request.form['nombreProductos']
        descripcionProductos = request.form['descripcionProductos']
        precioProductos = request.form['precioProductos']
        fechaLoteProductos = request.form['fechaLoteProductos']
        

        new_Productos = Productos(nombreProductos=nombreProductos, descripcionProductos=descripcionProductos, precioProductos=precioProductos, fechaLoteProductos=fechaLoteProductos)
        db.session.add(new_Productos)
        db.session.commit()
        
        return redirect(url_for('Productos.index'))

    return render_template('Productos/add.html')

@bp.route('/Productos/edit/<int:idProductos>', methods=['GET', 'POST'])
@login_required
def edit(idProductos):
    producto = Productos.query.get_or_404(idProductos)

    if request.method == 'POST':
        producto.nombreProductos = request.form['nombreProductos']
        producto.descripcionProductos = request.form['descripcionProductos']
        producto.precioProductos = request.form['precioProductos']
        producto.fechaLoteProductos = request.form['fechaLoteProductos']
        
        db.session.commit()
        return redirect(url_for('Productos.index'))

    return render_template('Productos/edit.html', producto=producto)
    

@bp.route('/Productos/delete/<int:idProductos>')
@login_required
def delete(idProductos):
    productos = Productos.query.get_or_404(idProductos)
    
    db.session.delete(productos)
    db.session.commit()

    return redirect(url_for('Productos1.index'))




