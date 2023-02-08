from flask import Flask, render_template, request , session, redirect
from user_model import User

app = Flask(__name__)
app.secret_key = 'secret fvbdfljvbdlfjvbldfjvnnjjn'

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/process", methods=["POST"])
def process_form():
    print(f"Form from request == {request.form}")
    session["username"] = request.form["username"]
    session["email"] = request.form["email"]
    session["age"] = request.form["age"]
    User.create_user(request.form)
    return redirect("/display")

@app.route("/display")
def display():
    users = User.get_all()
    return render_template("display.html", users=users)


@app.route("/user/<int:user_id>")
def show_user(user_id):
    data_dict = {'id': user_id}
    user = User.get_one(data_dict)
    return render_template("one_user.html" , user=user)


@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/display")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
