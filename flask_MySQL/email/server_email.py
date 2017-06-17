from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]=$')
app = Flask(__name__)

app.secret_key = '123456mysql = MySQLConnector(app, '')'

@app.route('/')
def index():
	query = 'SELECT * FROM emails'
	emails = mysql.query_db(query)
	return render_template('index.html', all_email = emails)

@app.route('/validate/<email_id>')
def show():
	query = 'SELECT * FROM  emails'
	data = email_id
	emails = mysql.query_db(query, data)
	return render_template('index.html')

@app.route('/validate', methods=['POST'])
def create():
	if len(request.form['email']) < 1:
		flash('email cannot be empty')
	elif not EMAIL_REGEX.match(request.form['emial']):
		flash('Invalid email address!!!!')
	else:
		flash('Success!!')
		query = 'INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
		data = {
				'email': request.form['email']
				}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)