from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user', methods=['POST'])
def create_user():
	name = request.form['name']
	email = request.form['email']
	return render_template('user.html')
@app.route('/user')
def show_user():
	print request.form['name']
	return render_template('user.html')

app.run(debug=True)