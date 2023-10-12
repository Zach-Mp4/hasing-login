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
    
    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8, email = email, first_name = first_name, last_name = last_name)
    

    
    
    
    