from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
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
        user_id = User.create_user(data)
        print("+"*20, user_id,"+"*20)
        session['user_id'] = user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id'  not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", logged_user = logged_user)

@app.route('/users/login', methods=['post'])
def login():
    # Verify Email
    data = {
        'email': request.form['email']
    }
    user_from_db = User.get_by_email(data)
    print("*"*20,user_from_db,"*"*20)
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        # if we get False after checking the password
            flash("Invalid Password","login")
            return redirect('/')
        else:
            session['user_id'] = user_from_db.id
            return redirect("/dashboard")
    flash("Invalid Email","login")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')