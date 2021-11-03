from models import Alumno
from json import loads
import jsonschema
from data.jsonschemas import esquema_alumno
from data import carreras


def convierte_a_dict(cuenta, alumno, esquema):
    respuesta = {'Cuenta': cuenta}
    for campo in esquema["properties"]:
        respuesta[campo] = getattr(alumno, campo.lower().replace(' ', '_'))
    return respuesta
    
def recurso_completo(cuenta, peticion):
    try:
        candidato = Alumno(cuenta=int(cuenta))
        peticion = loads(peticion)
        jsonschema.validate(peticion, esquema_alumno)
        if set(esquema_alumno["properties"]).issuperset(peticion) \
        and peticion["Carrera"] in carreras:
            for campo in peticion:
                setattr(candidato, campo.lower().replace(' ', '_'), peticion[campo])
        else:
            raise(TypeError, "Not valid")
    except (jsonschema.exceptions.ValidationError, TypeError):
        return None
    return candidato