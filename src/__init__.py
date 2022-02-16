#! /usr/bin/python3

from flask import abort, jsonify
from json import loads

carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura", "Administración")
orden = ('nombre', 'primer_apellido', 'segundo_apellido', 'carrera','semestre', 'promedio', 'al_corriente')
campos = {'cuenta': (int, True), 'nombre': (str, True), 'primer_apellido': (str, True), 'segundo_apellido': (str, False), 'carrera': (str, True), 'semestre': (int, True), 'promedio': (float, True), 'al_corriente': (bool, True)}

def carga_base(ruta):
    with open(ruta, 'tr') as base:
        return eval(base.read())


def escribe_base(lista ,ruta):
    with open(ruta, 'wt') as base:
            base.write(str(lista))

            
def busca_base(cuenta, base):
    for alumno in base:
        try:
            if alumno['cuenta'] == int(cuenta):
                return alumno
        except:
            return False
    return False


def es_tipo(dato, tipo):
    if tipo == str:
        return True
    else:
        try: 
            return tipo(dato) is dato
        except:
            return False


def reglas(dato, campo):
    if campo == "carrera" and dato not in carreras:
        return False
    elif campo == "semestre" and dato < 1:
        return False
    elif campo == "promedio" and (dato < 0 or dato > 10):
        return False
    elif (campo in ("nombre", "primer_apellido") and (dato == "")):
        return False
    else:
        return True


def valida(dato, campo):
    return es_tipo(dato, campos[campo][0]) and reglas(dato, campo)


def recurso_completo(base, ruta, cuenta, peticion):
    try:
        candidato = {'cuenta': int(cuenta)}
        peticion = loads(peticion)
        if (set(peticion)).issubset(set(orden)):                    
            for campo in orden:
                if not campos[campo][1] and campo not in peticion:
                    candidato[campo] = ''
                elif valida(peticion[campo], campo):
                    candidato[campo] = peticion[campo]      
                else:
                    abort(400)
        else:
            abort(400)
    except:
        abort(400)
    base.append(candidato)
    escribe_base(base, ruta)
    return jsonify(candidato)