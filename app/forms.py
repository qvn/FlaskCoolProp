from flask_wtf import Form
from wtforms import TextField, validators, DecimalField, SelectField
from wtforms.validators import DataRequired

class PressureForm(Form):
	Fluid = SelectField('Fluid', choices=[('Water', 'Water'), ('Pentane', 'Pentane'), ('Propane', 'Propane')])
	Pressure = DecimalField('Pressure', validators = [DataRequired()])
	Temperature = DecimalField('Temperature',validators = [DataRequired()])

