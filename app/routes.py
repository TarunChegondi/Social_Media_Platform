from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Post
from app.forms import LoginForm, RegistrationForm, PostForm

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
@main_routes.route('/index')
@login_required
def index():
    posts = Post.query.all()
    form = PostForm()
    return render_template('home.html', title='Home', form=form, posts=posts)

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main_routes.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main_routes.index'))
    return render_template('login.html', title='Sign In', form=form)

@main_routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_routes.index'))

@main_routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_routes.login'))
    return render_template('register.html', title='Register', form=form)

@main_routes.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main_routes.index'))
    return render_template('post.html', title='New Post', form=form)
