from flask import render_template, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features1.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')