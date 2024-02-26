from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Productos import Productos
from app.routes.Carrito_routes import carrito_ventas
from app import db
import os
from flask_login import login_required

bp = Blueprint("Productos", __name__)


@bp.route("/Productos")
@login_required
def index():
    data = Productos.query.all()

    return render_template(
        "Productos/index.html", data=data, t=carrito_ventas.tamañoD()
    )


@bp.route("/Productos/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        nombreProductos = request.form["nombreProductos"]
        descripcionProductos = request.form["descripcionProductos"]
        precioProductos = request.form["precioProductos"]
        fechaLoteProductos = request.form["fechaCaducidadProductos"]
        Imagen = request.files["nombreImagen"]

        new_Productos = Productos(
            nombreProductos=nombreProductos,
            descripcionProductos=descripcionProductos,
            precioProductos=precioProductos,
            fechaLoteProductos=fechaLoteProductos,
            nombreImagen=Imagen.filename,
        )
        guardarImagen(Imagen)
        db.session.add(new_Productos)
        db.session.commit()

        return redirect(url_for("Productos.index"))

    return render_template("Productos/add.html")


@bp.route("/Productos/edit/<int:idProductos>", methods=["GET", "POST"])
@login_required
def edit(idProductos):
    producto = Productos.query.get_or_404(idProductos)

    if request.method == "POST":

        producto.nombreProductos = request.form.get(
            "nombreProductos", producto.nombreProductos
        )
        producto.descripcionProductos = request.form.get(
            "descripcionProductos", producto.descripcionProductos
        )
        producto.precioProductos = request.form.get(
            "precioProductos", producto.precioProductos
        )
        producto.fechaLoteProductos = request.form.get(
            "fechaLoteProductos", producto.fechaLoteProductos
        )

        db.session.commit()
        return redirect(url_for("Productos.index"))

    return render_template("Productos/edit.html", producto=producto)


@bp.route("/Productos/delete/<int:idProductos>")
@login_required
def delete(idProductos):
    productos = Productos.query.get_or_404(idProductos)

    db.session.delete(productos)
    db.session.commit()
    return redirect(url_for("Productos.index"))


def guardarImagen(imagen):
    from run import app

    carpetaDestino = os.path.join(app.root_path, "static", "imagenes")
    imagen.save(os.path.join(carpetaDestino, imagen.filename))


def eliminar(idProductos):
    from run import app

    Productos = Productos.query.get_or_404(idProductos)
    ruta_imagen = os.path.join(
        app.root_path, "static", "imagenes", Productos.nombreImagen
    )

    if os.path.exists(ruta_imagen):
        os.remove(ruta_imagen)
