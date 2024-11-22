from flask import Blueprint, render_template, request, redirect, flash
from models import Diretor
from database import db

bp_diretor = Blueprint('diretor', __name__, template_folder="templates")

@bp_diretor.route("/")
def index():
    a = Diretor.query.all()
    return render_template("diretores.html", diretores=a)


@bp_diretor.route("/add")
def add():
    return render_template("diretores_add.html")


@bp_diretor.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    pais = request.form.get("pais")

    if nome and pais:
        db_diretor = Diretor(nome, pais)
        db.session.add(db_diretor)
        db.session.commit()
        flash("Diretor salvo!")
        return redirect("/diretores")
    else:
        flash("Preencha tudo!")
        return redirect("/diretores/add")


@bp_diretor.route("/remove/<int:id>")
def remove(id):
    a = Diretor.query.get(id)
    try:
        db.session.delete(a)
        db.session.commit()
        flash("Diretor removido!")
    except:
        flash("Diretor inválido!")
    return redirect("/diretores")


@bp_diretor.route("/edit/<int:id>")
def edit(id):
    a = Diretor.query.get(id)
    return render_template("diretores_editar.html", diretores=a)


@bp_diretor.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    pais = request.form.get("pais")
    id_diretor = request.form.get("id_diretor")
    
    if nome and pais and id_diretor:
        a = Diretor.query.get(id_diretor)
        a.nome = nome
        a.pais = pais
        db.session.commit()
        flash("Diretor editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/diretores")