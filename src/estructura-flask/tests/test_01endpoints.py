import pytest
from app import create_app
from apiflaskdemo.project.models import db, Alumno
from apiflaskdemo.project.schemas import AlumnoSchema
from flask import Request

app = create_app()

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client


def test_get_alumnos(client):
    r = client.get('/api/')
    assert r.status == '200 OK'
    data = r.get_json()
    assert type(data) is list
    for alumno in data:
        AlumnoSchema().load(data=alumno)