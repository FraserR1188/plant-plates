import os
from plantplates import app, db
from plantplates.models import User

admin_email = "fraserrobbie2@gmail.com"

with app.app_context():
    user = User.query.filter_by(email=admin_email).first()
    if user:
        user.is_admin = True
        db.session.commit()
        print(f"User {user.email} is now admin.")
    else:
        print("No user found with that email.")