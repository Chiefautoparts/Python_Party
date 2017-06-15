from flask import Flask, render_template, redirect, request, sessions, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.seccret_key = "album is intended for fish ears only."
mysql= MySQLConnector(app, '**database**')

@app.route('/')
def index():
	