from plantplates import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=TRUE)
    email = db.Column(db.String(25), unique=TRUE, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer)
    password_hash 

    def __repr__(self):
        return self.name



