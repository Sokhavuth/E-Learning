#controllers/index.py
import config, copy
from flask import render_template, request
from flask_classful import FlaskView, route
from models.userdb import Userdb

class Index(FlaskView):
    def __init__(self):
        self.vdict = copy.deepcopy(config.vdict)
        self.userdb = Userdb()

    @route('/')
    def index(self):
        return render_template('index.html', data=self.vdict)

    @route('/login/', methods=['GET', 'POST'])
    def login(self):
        if request.method == 'POST':
            email = request.form['femail']
            
            #if(self.userdb.check_username(username)):
            return render_template('dashboard.html', data=self.vdict)
        
        return render_template('login.html', data=self.vdict)

        