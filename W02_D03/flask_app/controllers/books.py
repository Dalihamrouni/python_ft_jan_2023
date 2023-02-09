from flask_app import  app

from flask import render_template, request , session, redirect
from flask_app.models.book_model import Book
from flask_app.models.user_model import User

@app.route("/book")
def add_book():
    users = User.get_all()
    return render_template("new_book.html", users = users)

@app.route("/books")
def all_books():
    books = Book.get_all()
    return render_template("all_books.html", books = books)

@app.route("/book/create", methods=["POST"])
def create_book():
    print(f"Form from request == {request.form}")
    Book.create_book(request.form)
    return redirect("/display")