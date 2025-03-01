from plantplates import db


# ------------------------------
# 1. User Model
# ------------------------------
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=TRUE)
    email = db.Column(db.String(25), unique=TRUE, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(255), nullable=False)

    # Relationships between the User model
    recipes = db.relationship('Recipe', back_populates='author', cascade='all, delete-orphan')
    articles = db.relationship('Article', back_populates='author', cascade='all, delete-orphan')
    reviews = db.relationship('Review', back_populates='author', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

# ------------------------------
# 2. Category Model
# ------------------------------
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # A category can have many recipes
    recipes = db.relationship('Recipe', back_populates='category')

    def __repr__(self):
        return f"<Category {self.id} {self.name}>"

