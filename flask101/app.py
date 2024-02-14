from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from forms import LoginForm

db = SQLAlchemy()
load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/db_name"

db.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ally'}
    posts = [
        {
            'author': {'username': 'Kenny'},
            'body': "Japan's SAKURA is beautiful!"
        },
        {
            'author': {'username': 'Mandy'},
            'body': "My baby is quite, right?"
        }
    ]
    return render_template(template_name_or_list='index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("User's {} Login request, Remember me = {}".format(
            form.username.data, form.remember_me.data
        ))
        return redirect('index')
    return render_template(template_name_or_list='login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
