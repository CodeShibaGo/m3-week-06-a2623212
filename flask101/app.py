from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    app.run()
