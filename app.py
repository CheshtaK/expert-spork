from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def marks():
	if request.method == 'POST':
		hours = float(request.form['hours'])


if __name__ == '__main__':
	app.run(debug = True)