from flask_wtf import FlaskForm
from wtforms import Form,StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class FormPel(FlaskForm):
   
    titulo=StringField('Titulo',validators=[DataRequired(message='llene este campo')])
    original=StringField('Titulo Original',validators=[DataRequired(message='llene este campo')])
    genero=StringField('Generos',validators=[DataRequired(message='llene este campo')])
    duracion=StringField('Duracion',validators=[DataRequired(message='llene este campo')])
    resumen=StringField('Resumen',validators=[DataRequired(message='llene este campo')])
    reparto=StringField('Reparto',validators=[DataRequired(message='llene este campo')])
    director=StringField('Director',validators=[DataRequired(message='llene este campo')])
    ingb=SubmitField('Ingresar Cambios')
    
