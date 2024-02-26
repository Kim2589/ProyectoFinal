from flask import Blueprint, render_template, request, redirect, url_for, jsonify, Flask
from app.models.Usuarios import Usuarios
from flask_login import login_required
from app import db
app = Flask(__name__)

bp = Blueprint('Usuarios', __name__)

@bp.route('/Usuarios')
@login_required
def index():
    print("Entra a usuarios")
    data = Usuarios.query.all()
    print("Entra a usuarios")

    return render_template('Usuarios/index.html', data=data)

@bp.route('/Usuarios/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        print(request.form)
        nombreUsuarios = request.form['nombreUsuarios']
        direccionUsuarios = request.form['direccionUsuarios']
        telefonoUsuarios = request.form['telefonoUsuarios']
        correoUsuarios = request.form['correoUsuarios']
        contrasenaUsuarios = request.form['contrasenaUsuarios']

        new_Usuarios = Usuarios(nombreUsuarios=nombreUsuarios, direccionUsuarios=direccionUsuarios, telefonoUsuarios=telefonoUsuarios, correoUsuarios=correoUsuarios,contrasenaUsuarios=contrasenaUsuarios )
        db.session.add(new_Usuarios)
        db.session.commit()
        
        return redirect(url_for('Usuarios.index'))

    return render_template('Usuarios/add.html')

@bp.route('/Usuarios/edit/<int:idUsuarios>', methods=['GET', 'POST'])
def edit(idUsuarios):
    usuario = Usuarios.query.get_or_404(idUsuarios)

    if request.method == 'POST':
        usuario.nombreUsuarios = request.form['nombreUsuarios']
        usuario.direccionUsuarios = request.form['direccionUsuarios']
        usuario.telefonoUsuarios = request.form['telefonoUsuarios']
        usuario.correoUsuarios = request.form['correoUsuarios']
        usuario.contrasenaUsuarios = request.form['contrasenaUsuarios']

        db.session.commit()
        return redirect(url_for('Usuarios.index'))

    return render_template('Usuarios/edit.html', usuario=usuario)
    

@bp.route('/Usuarios/delete/<int:idUsuarios>')
def delete(idUsuarios):
    Usuarios = Usuarios.query.get_or_404(idUsuarios)
    
    db.session.delete(Usuarios)
    db.session.commit()

    return redirect(url_for('Usuarios.index'))


