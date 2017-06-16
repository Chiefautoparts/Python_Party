from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]=$')
app = Flask(__name__)
app.secret_key = '123'
mysql = MySQLConnector(app,'mydb')
@app.route('/')
def index():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    # print friends
    return render_template('index.html', all_email=email)
@app.route('/validate/<email_id>')
def show(email_id):
    query = "SELECT * FROM email WHERE id = :specific_id"
    data = {'specific_id': email_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html',)
@app.route('/validate', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!") # just pass a string to the flash function
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
        'email': request.form['email']
        }
        # flash("Success! Your email is {}".format(request.form['email']))
    # print request.form['email']
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True