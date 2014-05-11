from flask_wtf import Form
from wtforms import TextField, validators, DecimalField
from wtforms.validators import DataRequired

class PressureForm(Form):
	Pressure = DecimalField('Pressure', validators = [DataRequired()])
	Temperature = DecimalField('Temperature',validators = [DataRequired()])

