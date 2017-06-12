from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index', methods=['POST'])
def process(name):
	name=request.form['name']
	return redirect('/')

@app.route('/process/<name>')
def show_name(name):
	print name
	return render_template('process.html')

app.run(debug=True)