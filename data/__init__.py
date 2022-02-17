#! /usr/bin/python3

# La ruta en la que se encuentra la base de datos.
ruta = 'data/alumnos.py'

# Define los campos que conforman la estructura de un mensaje completo. 
orden = ('nombre', 'primer_apellido', 'segundo_apellido', 'carrera','semestre', 'promedio', 'al_corriente')

# Indica el tipo de dato de cada campo en un registro de la base de datos, y si este es obligatorio (True).
campos ={'cuenta': (int, True), 'nombre': (str, True), 'primer_apellido': (str, True), 'segundo_apellido': (str, False), 'carrera': (str, True), 'semestre': (int, True), 'promedio': (float, True), 'al_corriente': (bool, True)}

# Listado de las cadenas de caracteres que deben aceptarse en el campo "Carreras". 
carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura", "Administración")

# JSONSchema para alumnos.
esquema_alumno = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "nombre": {"type": "string",
                   "minLength":1,
                   },
        "primer_apellido": {"type": "string", 
                   "minLength":1,},
        "segundo_apellido": {"type": "string", 
                   "minLength":1,},
        "carrera": {"type": "string"},
        "semestre": {"type": "number",
                   "minimum": 1,
                   "maximum": 50,},
        "promedio": {"type": "number",
                   "minimum": 0,
                   "maximum": 10,},
        "al_corriente": {"type": "boolean"},
    },
    "required": ["nombre",  "primer_apellido", "carrera", "semestre",
                 "promedio", "al_corriente"]
}   