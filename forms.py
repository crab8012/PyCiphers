from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CaesarForm(FlaskForm):
    string = StringField('String', validators=[DataRequired()])
    rotation = IntegerField('Rotation', validators=[DataRequired()])
    submit = SubmitField('SUBMIT')