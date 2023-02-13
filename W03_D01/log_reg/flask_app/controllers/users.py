from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# ============= Index Page=================
@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/users/register', methods=['post'])
def register():
    if User.validate(request.form):
        print("-"*20,request.form ['password'],"-"*20)
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        print("*"*20,hashed_password,"*"*20)
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password,
        }
        User.create_user(data)
    return redirect('/')