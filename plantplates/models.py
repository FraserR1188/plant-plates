from plantplates import db
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# ------------------------------
# 1. User Model
# ------------------------------
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(25), unique=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """Hashes a plaintext password and stores it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Compares a plaintext password with the stored hash."""
        return check_password_hash(self.password_hash, password)

    # Relationships between the User model
    recipes = db.relationship(
        'Recipe', back_populates='author',
        cascade='all, delete-orphan')
    articles = db.relationship(
        'Article', back_populates='author',
        cascade='all, delete-orphan')
    reviews = db.relationship(
        'Review', back_populates='author',
        cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.id} {self.email}>"


# ------------------------------
# 2. Category Model
# ------------------------------
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Relationship: one category can have many recipes
    recipes = db.relationship('Recipe', back_populates='category')

    def __repr__(self):
        return f"<Category {self.id} {self.name}>"


# ------------------------------
# 3. Recipe Model
# ------------------------------
class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(
        db.BigInteger, db.ForeignKey('users.id'),
        nullable=False)
    category_id = db.Column(
        db.BigInteger, db.ForeignKey('categories.id'),
        nullable=True)

    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    seasonal = db.Column(db.String(50), nullable=True)
    total_time = db.Column(db.Integer, nullable=True)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    steps_to_prepare = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    yield_ = db.Column(db.Integer, nullable=True)
    ingredients = db.Column(db.Text, nullable=False)
    calories = db.Column(db.Integer, nullable=True)

    # Relationships
    author = db.relationship('User', back_populates='recipes')
    category = db.relationship('Category', back_populates='recipes')
    reviews = db.relationship(
        'Review', back_populates='recipe',
        cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Recipe {self.id} {self.title}>"


# ------------------------------
# 4. Review Model
# ------------------------------
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.BigInteger, primary_key=True)
    recipe_id = db.Column(
        db.BigInteger, db.ForeignKey('recipes.id'),
        nullable=False)
    user_id = db.Column(
        db.BigInteger, db.ForeignKey('users.id'),
        nullable=False)

    rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False)

    # Relationships
    recipe = db.relationship('Recipe', back_populates='reviews')
    author = db.relationship('User', back_populates='reviews')

    def __repr__(self):
        return f"<Review {self.id} (Recipe {self.recipe_id})>"


# ------------------------------
# 5. Article Model
# ------------------------------
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(
        db.BigInteger, db.ForeignKey('users.id'),
        nullable=False)

    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)

    # Relationships
    author = db.relationship('User', back_populates='articles')

    def __repr__(self):
        return f"<Article {self.id} {self.title}>"
