from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField,DecimalField
from wtforms.validators import DataRequired



class Opinion(FlaskForm):
    pelicula = SelectField('Pelicula',choices=[])
    calificacion = DecimalField('Calificacion', validators=[DataRequired()])
    comentario = StringField('Comentario', validators=[DataRequired()])
    usuario = StringField('Usuario', validators=[DataRequired()])
    enviar = SubmitField('Enviar Comentario')