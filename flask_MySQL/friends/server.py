from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'rudy was offsides'
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
	friends = mysql.query_db('SELECT * FROM friends')
	print friends
	return render_template('index.html')
@app.route('/friends', methods=['POST'])
def create():
	print request.form['first_name']
	print request.form['last_name']
	print request.form['age']
	# return redirect('/')
# @app.route('/friends', methods=['POST'])
# def create():
	query = 'INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())'
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'age': request.form['age']
	}
	mysql.query_db(query, data)
	return redirect('/')
app.run(debug=True)