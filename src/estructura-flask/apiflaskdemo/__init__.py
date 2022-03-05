from apiflask import APIFlask
from apiflaskdemo.project.models import db, Alumno, User
from apiflaskdemo.project.blueprints import abc_alumnos
from apiflaskdemo.project.auth.blueprints import auth_bp
from sqlalchemy import engine, inspect

def create_app():
    '''Función principal de la aplicación'''
    # Crear el objeto app
    app = APIFlask(__name__)
    
    # Obtener la configuración de la aplicación a partir de settings.py
    app.config.from_pyfile("settings.py")
    
    # Se incializa la conexión entre SQLALchemy y la base de datos
    db.init_app(app) 
    
    @app.before_first_request
    def crea_bases():
        '''Función encargada de verificar que exista una base de datos  con
           las tablas de alumnos y de usuarios pobladas correctamente. 
            En caso de no existir, es creada'''
         
        # Verifica que exista la tabla alumno en la base de datos
        inspector = inspect(db.engine)
        if not inspector.has_table('alumno'):
            # Crea y llena la base de alumno.
            db.create_all()
            with open(app.config['PATH'] + "/../data/alumnos.txt", "rt") as f:
                alumnos = eval(f.read())
                for alumno in alumnos:
                    if Alumno.query.filter_by(cuenta=alumno["cuenta"]).first():
                        continue
                    else:
                        db.session.add(Alumno(**alumno))
                db.session.commit()
                
            # Verifica que exista el usuario admin y lo crea si no es así 
            if not User.query.filter_by(username="admin").first():
                user = User(username='admin',
                           email='example@example.com',
                           password='admin', 
                           active=True)
                db.session.add(user)
                db.session.commit()
                
    # Registra los blueprints con los endpoints
    app.register_blueprint(abc_alumnos, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    #Regresa la aplicación
    return app