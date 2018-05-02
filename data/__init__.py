#! /usr/bin/python3

# La ruta en la que se encuentra la base de datos.
ruta = 'data/alumnos.txt'

# Define los campos que conforman la estructura de un mensaje completo. 
orden = ('Nombre', 'Primer Apellido', 'Segundo Apellido', 'Carrera','Semestre', 'Promedio', 'Al Corriente')

# Indica el tipo de dato de cada campo en un registro de la base de datos, y si este es obligatorio (True).
campos ={'Cuenta': (int, True), 'Nombre': (str, True), 'Primer Apellido': (str, True), 'Segundo Apellido': (str, False), 'Carrera': (str, True), 'Semestre': (int, True), 'Promedio': (float, True), 'Al Corriente': (bool, True)}

# Listado de las cadenas de caracteres que deben aceptarse en el campo "Carreras". 
carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura", "Administración")