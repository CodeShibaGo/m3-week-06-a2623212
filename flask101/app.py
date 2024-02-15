from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
from dotenv import load_dotenv
from forms import LoginForm

db = SQLAlchemy()
load_dotenv()
app = Flask(__name__)
Migrate(app, db)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/MicroBlogData"

db.init_app(app)


class Users(db.Model):
    __tablename__ = 'users'
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column(db.String(100))
    mobile = db.Column('mobile', db.String(100))

    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile


sql = text('select * from users')
with app.app_context():
    result = db.session.execute(sql)
    print(result.fetchall())


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
