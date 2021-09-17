from flask_wtf import form
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterphonenumberForm
#from app.models import User, Post
#from flask_login import login_required, login_user, logout_user, current_user




@app.route('/')
#@login_required
def index():
#    all_posts = Post.query.all()
    return render_template('index.html', form=form)

