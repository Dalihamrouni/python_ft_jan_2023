from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.author import Author


@app.route("/")
def index():
    all_authors = Author.get_all()
    return render_template("index.html", all_authors=all_authors)

@app.route('/authors/new')
def new_author():
    return render_template("new_author.html")

@app.route('/authors/create', methods= ['post'])
def create_author():
    Author.create_author(request.form)
    return redirect('/')

@app.route('/authors/<int:author_id>/show')
def show_author(author_id):
    data_dict = {
        'id': author_id
    }
    this_author = Author.get_one(data_dict)
    #     this_author = Author.get_one({'id':author_id})
    return render_template ("show_author.html", this_author = this_author)

@app.route('/authors/<int:author_id>/edit')
def edit_author(author_id):
    this_author = Author.get_one({'id':author_id})
    return render_template("edit_author.html", this_author=this_author)

@app.route('/authors/update', methods=['post'])
def update_author():
    print("-"*20,request.form['id'],"-"*20)
    author_id = request.form['id']
    Author.update_author(request.form) 
    return redirect(f'/authors/{author_id}/show')

@app.route('/authors/<int:author_id>/delete')
def delete_author(author_id):
    Author.delete_author({'id': author_id})
    return redirect('/')