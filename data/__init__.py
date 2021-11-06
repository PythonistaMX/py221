#! /usr/bin/python3

# La ruta en la que se encuentra la base de datos.
ruta = 'data/alumnos.txt'

# Define los campos que conforman la estructura de un mensaje completo. 
orden = ('Nombre', 'Primer Apellido', 'Segundo Apellido', 'Carrera','Semestre', 'Promedio', 'Al Corriente')

# Indica el tipo de dato de cada campo en un registro de la base de datos, y si este es obligatorio (True).
campos ={'Cuenta': (int, True), 'Nombre': (str, True), 'Primer Apellido': (str, True), 'Segundo Apellido': (str, False), 'Carrera': (str, True), 'Semestre': (int, True), 'Promedio': (float, True), 'Al Corriente': (bool, True)}

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