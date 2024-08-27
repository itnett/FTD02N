python
from wtforms import StringField
from wtforms.validators import IPAddress

class IPForm(FlaskForm):
    ip_adresse = StringField('IP-adresse', validators=[IPAddress()])