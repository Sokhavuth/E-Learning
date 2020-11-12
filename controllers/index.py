#controllers/index.py
import config, copy
from flask import render_template, request, session, redirect
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
            password = request.form['fpassword']

            if(self.userdb.check_user(email, password)):
            if True:
                session['email'] = email
                return render_template('dashboard.html', data=self.vdict)
        
        else:
            if 'email' in session:
                return render_template('dashboard.html', data=self.vdict)
            
            return render_template('login.html', data=self.vdict)

    @route('/logout/')
    def logout(self):
        session.pop('email', None)
        return redirect('/')