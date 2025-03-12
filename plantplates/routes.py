import os
import boto3
from plantplates import app, db
from plantplates.models import User, Category, Recipe, Review, Article
from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

s3_client = boto3.client('s3')


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
            return redirect(url_for('account'))
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
        return redirect(url_for('account'))
    return render_template('signup.html')


@app.route('/account')
@login_required
def account():
    """Display the account page showing the logged-in user's details."""
    return render_template('account.html')


@app.route('/create_recipe', methods=['GET', 'POST'])
@login_required
def create_recipe():
    if request.method == 'POST':
        # Retrieve form data
        title = request.form.get('title')
        seasonal = request.form.get('seasonal')
        total_time = request.form.get('total_time')
        yield_ = request.form.get('yield')
        ingredients = request.form.get('ingredients')
        calories = request.form.get('calories')
        steps_to_prepare = request.form.get('steps_to_prepare')
        summary = request.form.get('summary')
        # Handle the file upload
        file = request.files.get('image_file')
        image_url = None
        
        if file and file.filename:
            import uuid
            from werkzeug.utils import secure_filename
            
            # Create a unique filename or object key (e.g., with a UUID)
            original_filename = secure_filename(file.filename)
            unique_id = str(uuid.uuid4())
            s3_key = f"recipe_images/{unique_id}_{original_filename}"

            # Upload to S3
            s3_client = boto3.client('s3')
            bucket_name = "plantplates-images"
            
            s3_client.upload_fileobj(
                file,
                bucket_name,
                s3_key,
                ExtraArgs={
                    'ContentType': file.content_type
                }
            )
            
            # Construct the image URL (if public is necessary)
            region = "eu-west-2"
            image_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{s3_key}"

        # Create a new Recipe object associated with the logged-in user
        new_recipe = Recipe(
            title=title,
            image_url=image_url,
            seasonal=seasonal,
            total_time=total_time,
            yield_=yield_,
            ingredients=ingredients,
            calories=calories,
            steps_to_prepare=steps_to_prepare,
            summary=summary,
            user_id=current_user.id
        )
        # Save the new recipe to the database
        db.session.add(new_recipe)
        db.session.commit()

        flash("Recipe created successfully!", "success")
        return redirect(url_for('my_recipes'))
    # GET request: Render the create recipe page
    return render_template('create_recipe.html')


@app.route('/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    # Fetch the recipe or return 404 if not found
    recipe = Recipe.query.get_or_404(recipe_id)
    # Only allow the owner to edit their recipe.
    if recipe.user_id != current_user.id:
        flash("You do not have permission to edit this recipe.", "error")
        return redirect(url_for('my_recipes'))
    if request.method == 'POST':
        # Update text fields
        recipe.title = request.form.get('title')
        recipe.seasonal = request.form.get('seasonal')
        recipe.total_time = request.form.get('total_time')
        recipe.yield_ = request.form.get('yield')
        recipe.ingredients = request.form.get('ingredients')
        recipe.calories = request.form.get('calories')
        recipe.steps_to_prepare = request.form.get('steps_to_prepare')
        recipe.summary = request.form.get('summary')
        # Optionally handle image file update
        file = request.files.get('image_file')
        if file and file.filename:
            filename = secure_filename(file.filename)
            # Optionally, check for allowed file extensions here
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            recipe.image_filename = filename  # Update the image filename
        db.session.commit()
        flash("Recipe updated successfully!", "success")
        return redirect(url_for('recipe_detail', recipe_id=recipe.id))
    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    # Ensure that only the owner can delete their recipe.
    if recipe.user_id != current_user.id:
        flash("You do not have permission to delete this recipe.", "error")
        return redirect(url_for('recipe_detail', recipe_id=recipe.id))
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted successfully!", "success")
    return redirect(url_for('my_recipes'))


@app.route('/my_recipes')
@login_required
def my_recipes():
    user_recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return render_template('my_recipes.html', recipes=user_recipes)


@app.route('/recipe/<int:recipe_id>')
@login_required
def recipe_detail(recipe_id):
    # Fetch the recipe from the DB; 404 if not found
    recipe = Recipe.query.get_or_404(recipe_id)

    return render_template('recipe_detail.html', recipe=recipe)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))


@app.route('/protected')
@login_required
def protected():
    return f"Hello, {current_user.email}! Only logged-in users can see this."
