#controllers/index.py
from flask_classful import FlaskView, route

class Index(FlaskView):
    @route('/')
    def index(self):
        return 'Hello World!!!'