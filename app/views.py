from app import app
from flask import render_template, flash, redirect, url_for
from forms import PressureForm
from CoolProps import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/pressure', methods=['GET','POST'])
def pressure():
	form = PressureForm()
	props = {}
	if form.validate_on_submit():
		fluid = form.Fluid.data
		flash = form.Flash.data
		prop1 = form.Prop1.data
		prop2 = form.Prop2.data
		props = CoolProp_State(flash,fluid,prop1,prop2).get_all()
		return render_template('PressureForm.html', form = form, props = props)
	return render_template('PressureForm.html', form=form, props = props)

if __name__ == '__main__':
    app.run(debug=True) #debug turned on. make sure to turn off during production
