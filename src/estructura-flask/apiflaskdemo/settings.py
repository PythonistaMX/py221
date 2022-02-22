'''Configuración de la aplicación.'''
import os

DEBUG = True
TESTING = False
PATH = os.path.dirname(os.path.abspath(__file__))
ENV = "development"
SECURITY_PASSWORD_SALT = 'ultra-secreto'
SECRET_KEY = "eaee87a94dc51d5412e4ed53a585cec2c92256f305ca8b41348c159adf4f045c"
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.alumnos.sql'
SQLALCHEMY_TRACK_MODIFICATIONS = False
