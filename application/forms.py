from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name= StringField("name",validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    completed= SelectField("Completed",choices=[("False","False"),("True","True")],validators=[DataRequired()]) #el nombre de la eleccion el False y tiene adjuntado un valor False cuando se selecciona
    submit=SubmitField("Add Todo")