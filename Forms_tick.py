from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField,DecimalField
from wtforms.validators import DataRequired

class Ticket(FlaskForm):
    funcion = SelectField('Pelicula',choices=['Funcion Estandar','Funcion VIP'])
    enviar = SubmitField('Enviar')
    cantidad=IntegerField('Cantidad', validators=[DataRequired()])


    