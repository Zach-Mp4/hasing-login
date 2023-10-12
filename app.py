from flask import Flask, render_template, redirect, session, flash
from models import connect_db, db, User
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///hashing_login"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"

connect_db(app)
# db.create_all()

@app.route('/')
def start():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        newUser = User.register(username, password, email, first_name, last_name)
        db.session.add(newUser)
        db.session.commit()
        return redirect('/secret')
    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', form = form)

@app.route('/secret')
def secret():
    return 'YOU MADE IT'
