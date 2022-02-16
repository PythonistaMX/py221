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
        "Nombre": {"type": "string",
                   "minLength":1,
                   },
        "Primer Apellido": {"type": "string", 
                   "minLength":1,},
        "Segundo Apellido": {"type": "string", 
                   "minLength":1,},
        "Carrera": {"type": "string"},
        "Semestre": {"type": "number",
                   "minimum": 1,
                   "maximum": 50,},
        "Promedio": {"type": "number",
                   "minimum": 0,
                   "maximum": 10,},
        "Al Corriente": {"type": "boolean"},
    },
    "required": ["Nombre",  "Primer Apellido", "Carrera", "Semestre",
                 "Promedio", "Al Corriente"]
}   