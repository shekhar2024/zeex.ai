from flask import render_template, url_for, redirect, request, flash
from app import app
from models import db, Message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Please fill out all fields')
        return redirect(url_for('contact'))

    message = Message(name=name, email=email, message=message)
    db.session.add(message)
    db.session.commit()

    flash('Message sent successfully')

    return redirect(url_for('contact'))

@app.route('/blog')
def blog():
    return render_template('blog1.html')