from database import db

class Diretor(db.Model):
    __tablename__ = 'diretors'
    id_diretor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    pais = db.Column(db.String(50))
   
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
    
    def __repr__(self):
        return f"<Diretor {self.nome}>"
    

class Filme(db.Model):
    __tablename__ = 'filme'
    id_filme = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100))
    ano_lanc = db.Column(db.String(50))
    id_diretor = db.Column(db.Integer, db.ForeignKey('diretors.id_diretor'))

    diretor = db.relationship('Diretor', foreign_keys=id_diretor)

    def __init__(self, titulo, ano_lanc, id_diretor):
        self.titulo = titulo
        self.ano_lanc = ano_lanc
        self.id_diretor = id_diretor
    
    def __repr__(self):
        return f"<Cadastro: {self.titulo} - {self.ano_lanc} - {self.id_diretor}> "