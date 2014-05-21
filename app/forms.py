from flask_wtf import Form
from wtforms import TextField, validators, DecimalField, SelectField
from wtforms.validators import DataRequired

class PressureForm(Form):
	Flash = SelectField('Flash', choices=[('PT', 'Pressure / Temperature'), ('PH', 'Pressure / Enthalpy'), ('PS', 'Pressure / Entropy')])
	Fluid = SelectField('Fluid', choices=[('Water', 'Water'), ('Pentane', 'Pentane'), ('Propane', 'Propane')])
	Prop1 = DecimalField('Prop1', validators = [DataRequired()])
	Prop2 = DecimalField('Prop2', validators = [DataRequired()])

