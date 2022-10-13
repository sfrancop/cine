from tkinter import E
from flask_wtf import FlaskForm
from wtforms import  Form,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Inicio(FlaskForm):
    usuario=StringField('nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    contraseña=PasswordField('contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    recordar=BooleanField('Recordar Usuario')
    enviar=SubmitField('Iniciar Sesion')

class Registro(FlaskForm):
    nombre=StringField('nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    apellido=StringField('apellido', validators=[DataRequired(message='No dejar vacio, completar')])
    contraseña=PasswordField('contraseña', validators=[DataRequired(message='No dejar vacio, completar')])