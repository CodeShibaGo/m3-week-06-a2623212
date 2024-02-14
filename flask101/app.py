from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)
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
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()
