from flask import render_template, redirect, request, url_for
""" from __init__ import app, db
from models.test import Tests

@app.route('/', methods=['GET'])
def exp_list():
	tests = Tests.query.all()
	return render_template('index.html', tests = tests) """

from __init__ import app

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)