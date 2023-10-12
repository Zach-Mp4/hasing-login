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
        try:
            db.session.add(newUser)
            db.session.commit()
            session["user_id"] = newUser.username
            return redirect(f'/users/{session["user_id"]}')
        except:
            flash('duplicate user try logging in!')
            return redirect('/register')


    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        curUser = User.authenticate(username, password)
        if curUser:
            session["user_id"] = curUser.username
            return redirect(f'/users/{session["user_id"]}')
        flash('incorrect username or password')
        return redirect('/login')
    return render_template('login.html', form = form)

@app.route('/users/<username>')
def user_route(username):
    try:
        if session["user_id"]:
            curUser = User.query.get_or_404(username)

            userDict = curUser.dictUser()
            return render_template('user.html', user = userDict)
    except:
        return redirect('/register')

@app.route('/logout')
def logout():
    session.pop("user_id")

    return redirect("/")
