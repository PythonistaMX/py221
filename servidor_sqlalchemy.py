
# coding: utf-8

# **Advertencia:** Es necesario que se haya creado correctamente la base de datos localizada en [data/alumnos.db]([data/alumnos.db).

# ## Importación de módulos y datos.

from flask import Flask, jsonify, request, abort
from data import campos, orden
from json import loads
from flask_sqlalchemy import SQLAlchemy


# ## Creación de la aplicación e inicio de la sesión con la base de datos.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/alumnos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ## Definición de la clase *Alumno*.

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    cuenta = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    primer_apellido = db.Column(db.String(50))
    segundo_apellido = db.Column(db.String(50))
    carrera = db.Column(db.String(50))
    semestre = db.Column(db.Integer)
    promedio = db.Column(db.Float)
    al_corriente = db.Column(db.Boolean)


# ## Función de conversión de los objetos a objetos tipo _dict_.
# 
# Para poder enviar los datos a través de la API es necesario convertir los atributos de los objetos instanciados de la clase *Alumno* en campos de una objeto *dict*.

def convierte(cuenta, alumno, orden):
    respuesta = {'cuenta': cuenta}
    for campo in orden:
        respuesta[campo] = getattr(alumno, campo.lower().replace(' ', '_'))
    return respuesta


# ## Funciones de validación de datos.
# 
# Estaas funciones no fueron modificadas con respecto al capítulo previo.

def es_tipo(dato, tipo):
    if tipo == str:
        return True
    else:
        try: 
            return tipo(dato) is dato
        except:
            return False
        
def reglas(dato, campo):
    from data import carreras
    if campo == "Carrera" and dato not in carreras:
        return False
    elif campo == "Semestre" and dato < 1:
        return False
    elif campo == "Promedio" and (dato < 0 or dato > 10):
        return False
    elif (campo in ("Nombre", "Primer Apellido") and (dato == "")):
        return False
    else:
        return True           
    
def valida(dato, campo):
    return es_tipo(dato, campos[campo][0]) and reglas(dato, campo)


# ## La función *recurso_completo()*.
# Esta función fue modificada para poder gestionar objetos instanciados de *Alumno* y añadir registros a la base de datos.


def recurso_completo(cuenta, peticion):
    try:
        candidato = Alumno(cuenta=int(cuenta))
        peticion = loads(peticion)
        if (set(peticion)).issubset(set(orden)):                    
            for campo in orden:
                if not campos[campo][1] and campo not in peticion:
                    setattr(candidato, campo.lower().replace(' ', '_'), '')
                elif valida(peticion[campo], campo):
                    setattr(candidato, campo.lower().replace(' ', '_'), peticion[campo])    
                else:
                    abort(400)
        else:
            abort(400)
    except:
        abort(400)
    db.session.add(candidato)
    db.session.commit()                        
    return jsonify(convierte(cuenta, candidato, orden))


# ## Las funciones de vista.
# 
# Las funciones de vista conservan una estructura lógica idéntica, pero fueron modificadas para manipular los objetos instanciados de *Alumno* y realizar operaciones de búsqueda, modificación y eliminación de registros en la base de datos.

@app.route('/api/')
def ruta_api():
    lista = Alumno.query.filter(Alumno.cuenta).all()
    return jsonify([convierte(registro.cuenta, registro, orden) for registro in lista])
    

@app.route('/api/<cuenta>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def api(cuenta):
    
    if request.method == 'GET':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno == None:
            abort(404)
        else:
            return jsonify(convierte(cuenta, alumno, orden))
            
            
    if request.method == 'DELETE':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno == None:
            abort(404)
        else:
            db.session.delete(alumno)
            db.session.commit()
            return jsonify(convierte(cuenta, alumno, orden))
        
        
    if request.method == 'POST':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno == None:
            return recurso_completo(cuenta, request.data)
        else:
            abort(409)
            
            
    if request.method == 'PUT':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno == None:
            abort(404)
        else:
            db.session.delete(alumno)
            db.session.commit()
            return recurso_completo(cuenta, request.data)

    if request.method == 'PATCH':               
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno == None:
            abort(404)
        else:
            try:
                peticion = loads(request.data)
                if (set(peticion)).issubset(set(orden)):
                    for campo in peticion:
                        dato = peticion[campo]
                        if valida(dato, campo):
                            setattr(alumno, campo.lower().replace(' ', '_'), dato)
                        else:
                            abort(400)
                else:
                    abort(400)
            except:
                abort(400)
            db.session.add(alumno)
            db.session.commit()                        
            return jsonify(convierte(cuenta, alumno, orden))

