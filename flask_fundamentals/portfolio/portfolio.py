from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def homePage():
	return render_template('index.html')

@app.route('/about')
def otherPage():
	return render_template('about.html')

@app.route('/projects')
def lastPage():
	return render_template('projects.html')

app.run(debug=True)