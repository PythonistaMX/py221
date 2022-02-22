from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin

db = SQLAlchemy()

class Alumno(UserMixin, db.Model):
    __tablename__ = 'alumnos'
    cuenta = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    primer_apellido = db.Column(db.String(50))
    segundo_apellido = db.Column(db.String(50))
    carrera = db.Column(db.String(50))
    semestre = db.Column(db.Integer)
    promedio = db.Column(db.Float)
    al_corriente = db.Column(db.Boolean)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username= db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    authenticated = db.Column(db.Boolean())
