from wtforms import Form
from wtforms import TextField, validators, BooleanField, FloatField

class PressureForm(Form):
	Pressure = FloatField('Pressure', [validators.Required()])
	Temperature = FloatField('Temperature',[validators.Required()])

