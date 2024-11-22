from flask import Blueprint, render_template, request, redirect, flash
from models import Filme, Diretor
from database import db

bp_filme = Blueprint('filme', __name__, template_folder="templates")

@bp_filme.route("/")
def index():
    c = Filme.query.all()
    return render_template("filmes.html", filmes=c)


@bp_filme.route("/add")
def add():
    a = Diretor.query.all()
    return render_template("filmes_add.html", diretors=a)


@bp_filme.route("/save", methods=['POST'])
def save():
    titulo = request.form.get("titulo")
    ano_lanc = request.form.get("ano_lanc")
    id_diretor = request.form.get("id_diretor")

    if titulo and ano_lanc and id_diretor:
        db_filme = Filme(titulo, ano_lanc, id_diretor)
        db.session.add(db_filme)
        db.session.commit()
        flash("Filme salvo!")
        return redirect("/filmes")
    else:
        flash("Preencha tudo!")
        return redirect("/filmes/add")


@bp_filme.route("/remove/<int:id>")
def remove(id):
    c = Filme.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("Filme removido!")
    except:
        flash("Filme inválido!")
    return redirect("/filmes")


@bp_filme.route("/edit/<int:id>")
def edit(id):
    c = Filme.query.get(id)
    a = Diretor.query.all()
    return render_template("filmes_editar.html", filmes=c, diretors=a)


@bp_filme.route("/edit-save", methods=['POST'])
def edit_save():
    titulo = request.form.get("titulo")
    ano_lanc = request.form.get("ano_lanc")
    id_diretor = request.form.get("id_diretor")
    id_filme = request.form.get("id_filme")
    
    if titulo and ano_lanc and id_filme and id_diretor:
        c = Filme.query.get(id_filme)
        c.titulo = titulo
        c.ano_lanc = ano_lanc
        c.id_diretor = id_diretor
        db.session.commit()
        flash("Filme editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/filmes")