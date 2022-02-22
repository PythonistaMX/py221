'''Blueprints de la aplicación.'''
from flask import Blueprint, request, abort, jsonify
from models import db, Alumno
from functions import *
abc_alumno = Blueprint('abc_alumno', __name__)


@abc_alumno.route('/', methods=['GET'])
def muestra_alumnos():
    alumnos = Alumno.query.all()
    return jsonify([convierte_a_dict(alumno.cuenta, alumno, esquema_alumno) for alumno in alumnos])


@abc_alumno.route('/<cuenta>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def ops_alumno(cuenta):
    if request.method == 'GET':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            return jsonify(convierte_a_dict(cuenta, alumno, esquema_alumno))
        else:
            abort(404)
    if request.method == 'DELETE':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            db.session.delete(alumno)
            db.session.commit()
            return jsonify(convierte_a_dict(cuenta, alumno, esquema_alumno))
        else:
            abort(404)      
    if request.method == 'POST':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            abort(403)
        else:
            respuesta = recurso_completo(cuenta, request.data)
            if respuesta:
                db.session.add(respuesta)
                db.session.commit()
                return jsonify(convierte_a_dict(cuenta, respuesta, esquema_alumno))
            else:
                abort(406)
    if request.method == 'PUT':
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            respuesta = recurso_completo(cuenta, request.data)
            if respuesta:
                db.session.delete(alumno)
                db.session.add(respuesta)
                db.session.commit()
                return jsonify(convierte_a_dict(cuenta, respuesta, esquema_alumno))
            else:
                abort(406)
        else:
            
            abort(404) 
                