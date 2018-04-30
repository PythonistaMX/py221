from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return('<p>Hola, Mundo.</p>')

#Si no se define el parámetro host, flask sólo será visible desde localhost
# app.run(host='localhost')
app.run(host='0.0.0.0')