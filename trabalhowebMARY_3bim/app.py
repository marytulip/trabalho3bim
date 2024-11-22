from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha'
conexao = "mysql+pymysql://diretores:cefetmg@127.0.0.1/trab"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Diretor, Filme
db.init_app(app)
migrate = Migrate(app, db)

from modulos.diretores.diretores import bp_diretor
app.register_blueprint(bp_diretor, url_prefix='/diretores')
from modulos.filmes.filmes import bp_filme
app.register_blueprint(bp_filme, url_prefix='/filmes')

@app.route("/")
def index():
    return render_template("index.html")