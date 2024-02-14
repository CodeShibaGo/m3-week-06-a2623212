from flask import Flask, render_template
from dotenv import load_dotenv
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
load_dotenv()


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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template(template_name_or_list='login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
