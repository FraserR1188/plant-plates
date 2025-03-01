from plantplates import app, db
from plantplates.models import User, Category, Recipe, Review, Article
from flask import render_template, request, flash, redirect, url_for

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user)

# Initialize db with app
db.init_app(app)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # The endpoint name for your login page


@app.route("/")
def home():
    return render_template("home.html")


@login_manager.user_loader
def load_user(user_id):
    """Flask-Login calls this to get a user by ID."""
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            # Valid credentials
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for('protected'))
        else:
            # Invalid credentials
            flash("Invalid email or password.", "error")

    return render_template('login.html')  # Renders a simple login form


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')  # Optional field for user's name

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("A user with that email already exists.", "error")
            return redirect(url_for('signup'))

        # Create a new user and hash the password
        new_user = User(email=email, name=name)
        # Ensure your User model has set_password defined
        new_user.set_password(password)

        # Add and commit the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! You are now logged in.")
        login_user(new_user)  # Log the user in automatically after signup
        return redirect(url_for('protected'))
    return render_template('signup.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))


@app.route('/protected')
@login_required
def protected():
    return f"Hello, {current_user.email}! Only logged-in users can see this."
