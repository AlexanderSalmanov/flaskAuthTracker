from flask_login import UserMixin

from extensions import db, login_manager
from helpers import CRUDMixin


class AnonymousUser(CRUDMixin, db.Model):
    ip_address = db.Column(db.String(50), unique=True)

    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __repr__(self):
        return f"<AnonymousUser {self.ip_address}>"


class User(UserMixin, CRUDMixin, db.Model):
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.email}>"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
