from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """users model 😁"""
    __tablename__ = 'users'

    username = db.Column(db.Text,
                         primary_key=True)
    password = db.Column(db.Text,
                         nullable = False)
    email = db.Column(db.Text,
                      nullable = False,
                      unique = True)
    first_name = db.Column(db.Text,
                           nullable = False)
    last_name = db.Column(db.Text,
                           nullable = False)
    

    
    
    
    