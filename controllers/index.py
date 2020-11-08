#controllers/index.py
from flask import render_template
from flask_classful import FlaskView, route

class Index(FlaskView):
    def __init__(self):
        pass

    @route('/')
    def index(self):
        return render_template('index.html', data={'blogTitle':'រៀន​ពីចំងាយ'})