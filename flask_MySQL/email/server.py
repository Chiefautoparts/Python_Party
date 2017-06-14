from flask import Flask, render_template, sessions, redirect, request, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.seccret_key = 'watching Jaws backwards is a movie about a shark who vomits up people until a beach is opened'
mysql = MySQLConnector(app, 'emaildb')

@app.route('/')
def index():
	query = 'SELECT * FROM users'
	email = mysql.query_db(query)
	return render_template('index.html', all_email=emails)

@app.route('/email', methods=['POST'])
def create():
	print request.form['email']
	query = 'INSERT INTO email (email)'
	data = {
			'email': request.form['email']
			}
	mysql.query_db(query, data)
	return redirect('/')

# @app.route('/email' methods=['POST'])
# def checkValid():
# 	request.form(email)
# 	if email in users == null:
# 		print "	NICE TRY THERE BUCKOO. THAT'S NOT A VALID EMAIL"
# 	else:
# 		return redirect('/success')
app.run(debug=True)
