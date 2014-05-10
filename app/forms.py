from wtforms import Form
from wtforms import TextField, validators, BooleanField

class PressureForm(Form):
	Pressure = TextField('Pressure', [validators.Required()])

