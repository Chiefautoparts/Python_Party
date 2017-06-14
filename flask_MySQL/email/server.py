from flask import Flask, render_template, sessions, redirect, request, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.seccret_key = 'watching Jaws backwards is a movie about a shark who vomits up people until a beach is opened'
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
	query = 'SELECT * FROM users'
	users = mysql.query_db(query)
	return render_template('sucess.html', all_email=users)

@app.route('/email', methods=['POST'])
def create():
	print request.form['users']
	query = 'INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
	data = {
			'email': request.form['users']
			}
	mysql.query_db(query, data)
	# return redirect('sucess.html')
	return render_template('sucess.html', email=users(query, data))
	return redirect('sucess.html')
# @app.route('/email' methods=['POST'])
# def checkValid():
# 	request.form(email)
# 	if email in users == null:
# 		print "	NICE TRY THERE BUCKOO. THAT'S NOT A VALID EMAIL"
# 	else:
# 		return redirect('/success')
	
app.run(debug=True)
