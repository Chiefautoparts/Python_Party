from flask import Flask, render_template, redirect, request, sessions, flash, url_for
from mysqlconnection import MySQLConnector
from  flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]=$')
app = Flask(__name__)
bcrypt=Bcrypt(app)
app.secret_key = "album is intended for fish ears only"
mysql= MySQLConnector(app, 'registerdb')

@app.route('/')
def index():
	query = 'SELECT * FROM users'
	users = mysql.query_db(query)
	return render_template('index.html', Big='This my website', yell="go on get!")
	session['email']=request_form['email']
	session['password']=request_form['password']
	

@app.route('/login', methods=['POST'])
def login():
	# print request.form['first_name']
	# print request.form['last_name']
	print request.form['email']
	print request.form['password']
	# print request.form['confirm_password']
	query = 'INSERT INTO users (email, password, created_at, updated_at) VALUES (:email, :password, NOW(), NOW())'
	data = {
			# 'first_name': request.form['first_name'],
			# 'last_name': request.form['last_name'],
			'email': request.form['email'],
			'password': request.form['password'],
			# 'confirm_password': request.form['confirm_password']
			}
	
	if len(request.form['email']) < 1:
		flash("Email is empty dumbass......")
		
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Valid your email is not")
		
	else:
		flash("DAMSON your email is fly")
		return redirect('/success.html')

	mysql.query_db(query, data)
	return render_template('/success.html')
@app.route('/register', methods=['POST'])
def register():
		return render_template('/register.html')

@app.route('/create', methods=['POST'])
def create():
	print request.form['first_name']
	print request.form['last_name']
	print request.form['email']
	print request.form['password']
	print request.form['confirm_password']

	query = 'INSERT INTO users (first_name, last_name, email, password, confirm_password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :confirm_password, NOW(), NOW())'
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'password': request.form['password'],
			'confirm_password': request.form['confirm_password']
			}
	if len(request.form['email']) < 1:
		flash("If you don't put in your email Big Tony will break your kneecaps")

	elif not EMAIL_REGEX.match(request.form['email']):
		flash("input a real email.... I am watching you BUDDY")
	else:
		flash("PROUD OF YOU!")

	mysql.query_db(query, data)
	return render_template('/success.html')
	
app.run(debug=True)