'''Módulo principal de la aplicación.'''
from flask import Flask, request, abort
from flask_restful import Api, Resource
from models import db, Alumno
from functions import *

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
api = Api(app)
db.init_app(app)

class MuestraAlumnos(Resource):
    
    
    def get(Resource):
        alumnos = Alumno.query.all()
        return [convierte_a_dict(alumno.cuenta, alumno, esquema_alumno) for alumno in alumnos]
    

class ABCAlumno(Resource):
    
    
    def get(self, cuenta):
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            return convierte_a_dict(cuenta, alumno, esquema_alumno)
        else:
            abort(404)
    
    
    def delete(self, cuenta):
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            db.session.delete(alumno)
            db.session.commit()
            return convierte_a_dict(cuenta, alumno, esquema_alumno)
        else:
            abort(404)
     
    
    def post(self, cuenta):
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            abort(403)
        else:
            respuesta = recurso_completo(cuenta, request.data)
            if respuesta:
                db.session.add(respuesta)
                db.session.commit()
                return convierte_a_dict(cuenta, respuesta, esquema_alumno)
            else:
                abort(406)
     
    
    def put(self, cuenta):
        alumno = Alumno.query.filter_by(cuenta=cuenta).first()
        if alumno:
            respuesta = recurso_completo(cuenta, request.data)
            if respuesta:
                db.session.delete(alumno)
                db.session.add(respuesta)
                db.session.commit()
                return convierte_a_dict(cuenta, respuesta, esquema_alumno)
            else:
                abort(406)
        else:
            
            abort(404) 

api.add_resource(ABCAlumno, '/api/<string:cuenta>')
api.add_resource(MuestraAlumnos, '/api/')
            
if __name__ == '__main__':
    app.run(host='0.0.0.0')