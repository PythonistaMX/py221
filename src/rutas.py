#! /usr/bin/python3

from flask import Flask
app =Flask(__name__)


@app.route('/')
def inicio():
    return('<p>Hola, Mundo.</p>')
    
    
@app.route('/<usuario>')
def ruta_dinamica(usuario):
    return('<p>Hola, {}.</p>'.format(usuario))

app.run(host="0.0.0.0")