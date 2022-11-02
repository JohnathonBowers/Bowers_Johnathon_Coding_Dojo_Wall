from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.comment import Comment
from flask_app.models.post import Post
from flask_app.models.user import User

@app.route('/')
def a_go_home():   # The "a" in the function name stands for "action," since I'm neither rendering a template nor submitting a form
    return redirect ('/login')

@app.route('/login')
def r_login_registration():
    return render_template ('/')