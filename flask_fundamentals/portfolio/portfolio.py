from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def homePage():
	return render_template('index.html')

def otherPage():
	return render_template('pageone.html')

def lastPage():
	return render_template('pagetwo.html')

app.run(debug=True)