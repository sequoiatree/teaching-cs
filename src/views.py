from flask import render_template

from app import app
from models import WEEKS
from semester import SEMESTER

def rename(name):
    def rename_decorator(function):
        function.__name__ = name
        return function
    return rename_decorator

def make_template(week, type):
    @app.route(f'/{week.route(type)}.html')
    @rename(week.renderer(type))
    def render_resource():
        return render_template(week.template(type), resource=resource)

@app.route('/')
def render_index():
    return render_template('index.html', WEEKS=WEEKS, **SEMESTER)

@app.route('/policies')
def render_policies():
    return render_template('policies.html')

for week in WEEKS:
    make_template(week, 'homework')
    make_template(week, 'readings')
    make_template(week, 'journal')
