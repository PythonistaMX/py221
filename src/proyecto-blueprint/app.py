'''Módulo principal de la aplicación.'''
from flask import Flask
from models import db
from blueprints import abc_alumno
app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
db.init_app(app)
app.register_blueprint(abc_alumno, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0')