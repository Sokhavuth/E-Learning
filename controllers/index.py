#controllers/index.py
import config, copy
from flask import render_template, redirect
from flask_classful import FlaskView, route

class Index(FlaskView):
    def __init__(self):
        self.vdict = copy.deepcopy(config.vdict)

    @route('/')
    def index(self):
        return render_template('index.html', data=self.vdict)

    @route('/favicon.ico')
    def favicon():
        redirect('/static/images/site_logo.png')