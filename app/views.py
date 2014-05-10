from app import app
from flask import render_template
from forms import PressureForm

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/pressure', methods=['GET','POST'])
def pressure():
	form = PressureForm()
	return render_template('PressureForm.html', form=form)

if __name__ == '__main__':
    app.run(debug=True) #debug turned on. make sure to turn off during production
