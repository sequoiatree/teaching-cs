from flask import Flask
from flask_frozen import Freezer
from jinja2 import ChoiceLoader, FileSystemLoader

from models import WEEKS

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.jinja_loader = ChoiceLoader([
    app.jinja_loader,
    FileSystemLoader([week.path for week in WEEKS]),
])

freezer = Freezer(app)
