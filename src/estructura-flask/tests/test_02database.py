import pytest
from apiflaskdemo import create_app
from apiflaskdemo.project.models import Alumno, User, db
from apiflaskdemo.project.schemas import AlumnoSchema
from sqlalchemy import inspect

app = create_app()


@pytest.fixture
def base_conectada():
    print("Conectando a base de datos...")
    with app.app_context() as conectada:
        db.init_app(app)
        yield conectada


def test_existe_admin(base_conectada):
    print("Probando si existe el usuario 'admin...'")
    assert User.query.filter_by(username="admin")


def test_existe_tabla_alumnos(base_conectada):
    print('Probando que existan alumnos...')
    assert Alumno.query.all()
    
    
def test_datos_correctos_alumnos(base_conectada):
    print('Probando que los datos de los alumnos sean correctos..')
    
    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
    
    for alumno in Alumno.query.all():
        AlumnoSchema().load(data=object_as_dict(alumno))