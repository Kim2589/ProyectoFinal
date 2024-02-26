from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.Usuarios import Usuarios
from app.models.Empleados import Empleados


bp = Blueprint("Auth", __name__)


@bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nombreUsuarios = request.form["nombreUsuarios"]
        contrasenaUsuarios = request.form["contrasenaUsuarios"]

        usuarios = Usuarios.query.filter_by(
            nombreUsuarios=nombreUsuarios, contrasenaUsuarios=contrasenaUsuarios
        ).first()

        if usuarios:
            login_user(usuarios)
            return redirect(url_for("Auth.Iniciar"))

        empleados = Empleados.query.filter_by(
            nombreEmpleados=nombreUsuarios, contrasenaEmpleados=contrasenaUsuarios
        ).first()
        
        
        if empleados:
            login_user(empleados)
            return redirect(url_for("Productos.index"))

        flash("Invalid credentials. Please try again.", "danger")
    return render_template("Auth/login.html")


@bp.route("/Iniciar")
def Iniciar():
    return redirect(url_for("Productos1.index"))


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return render_template("Auth/login.html")
