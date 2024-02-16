from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from config import Config


app = Flask(__name__)
load_dotenv()
app.config.from_object(Config)
db = SQLAlchemy()
Migrate(app, db)
db.init_app(app)

from app import routes, models
