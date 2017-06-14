from flask import Flask, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'some string'

mysql = MySQLConnector(app, 'world')

print mysql.query_db('SELECT * FROM countries LIMIT 12')

app.run(debug=true)