python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    brukernavn = StringField('Brukernavn', validators=[DataRequired()])
    passord = PasswordField('Passord', validators=[DataRequired()])
    submit = SubmitField('Logg inn')