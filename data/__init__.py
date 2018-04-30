#! /usr/bin/python3

ruta = 'data/alumnos.txt'
orden = ('Nombre', 'Primer Apellido', 'Segundo Apellido', 'Carrera','Semestre', 'Promedio', 'Al Corriente')
campos ={'Cuenta': (int, True), 'Nombre': (str, True), 'Primer Apellido': (str, True), 'Segundo Apellido': (str, False), 'Carrera': (str, True), 'Semestre': (int, True), 'Promedio': (float, True), 'Al Corriente': (bool, True)}
carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura", "Administración")