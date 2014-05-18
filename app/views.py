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
	if form.validate_on_submit():
		t = form.Temperature.data
		p = form.Pressure.data
		State = CoolProp_State(p,t)
		rho = State.state.get_rho()
		cv = State.get_cv()
		cp = State.state.get_cp()
		flash('Completed Calculations')
		return render_template('PressureForm.html', form = form, p=p, T=t, rho = rho, Cv=cv, Cp = cp)
	return render_template('PressureForm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True) #debug turned on. make sure to turn off during production
