#controllers/login.py
import config, copy
from flask import render_template, request, session, redirect
from flask_classful import FlaskView, route
from models.userdb import Userdb

class Login(FlaskView):
  def __init__(self):
    self.userdb = Userdb()

  @route('/', methods=['GET', 'POST'])
  def login(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ទំព័រ​ចុះឈ្មោះ'

    user = self.userdb.select(1)
    if not user:
      return redirect('/dashboard/signup/')

    if request.method == 'POST':
      email = request.form['femail']
      password = request.form['fpassword']

      if(self.userdb.check_user(email, password)):
        session['logged-in'] = email
        return redirect('/dashboard/')
        
    else:
      if 'logged-in' in session:
        return redirect('/dashboard/')
            
      return render_template('login.html', data=vdict)

  @route('/logout/')
  def logout(self):
    session.pop('logged-in', None)
    return redirect('/')

login = Login()