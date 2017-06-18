from flask import Flask, render_template, sessions, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]=$')

app = Flask(__name__)
app.secret_key = 'watching Jaws backwards is a movie about a shark who vomits up people until a beach is opened'
mysql = MySQLConnector(app, 'emailsdb')

@app.route('/')
def index():
	query = 'SELECT * FROM email'
	email = mysql.query_db(query)
	return render_template('index.html', all_email=users)
	session['email']=request_form['email']
@app.route('/email', methods=['POST'])
def create():
	print request.form['email']
	query = 'INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
	data = {
			'email': request.form['email']
			}
	if len(request.form['email']) < 1:
		flash("Nothing entered in input field")
		
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email entered is not valid. try again")
		
	else:
		flash("BAAAAAMMMMMMMMMMMM!!!!!!!")
		return redirect('/success.html')
	
	return render_template('/success.html')
app.run(debug=True)
