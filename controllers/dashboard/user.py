#controllers/dashboard/user.py
import config, copy, lib, datetime
from flask import render_template, session, request, redirect
from models.userdb import Userdb

class User():
  def __init__(self):
    self.userdb = Userdb()
    self.lib = lib.Lib()

  def get_post_user(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ទំព័រ​អ្នក​ប្រើប្រាស់'
    vdict['datetime'] = self.lib.get_timezone()

    if (request.method == "POST"):
      email = request.form['fuser-title']
      password = request.form['fpassword']

      if not email:
        vdict['message'] = 'ចាំបាច់​ត្រូវ​មាន​ E-MAIL!'
        return render_template('dashboard/signup.html', data=vdict)

      if (self.userdb.check_user(email)) and (not ('edit' in session)):
        vdict['message'] = 'E-MAIL នេះ​ត្រូវ​បាន​គេ​យក​ទៅ​ប្រើប្រាស់​ហើយ។'
        return render_template('dashboard/signup.html', data=vdict)
        
      content = request.form['fcontent']
      role = request.form['fuser-role']
      date = request.form['fuser-date']
      time = request.form['fuser-time']
      if 'logged-in' in session:
        author = session['logged-in']
        author_role = self.userdb.check_author(author)
      else:
        author = 'root'

      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/signup.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/signup.html', data=vdict)

      if 'edit' in session:
        if author_role[3] == 'Admin':
          id = session['edit']
          self.userdb.update(email, password, role, content, date, time, author, id)
          session.pop('edit', None)
      else:
        if not self.userdb.select(1):
          self.userdb.insert(email, password, role, content, date, time, author)
        elif author_role[3] == 'Admin':
          self.userdb.insert(email, password, role, content, date, time, author)

      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 4, type='user')

      return render_template('dashboard/signup.html', data=vdict)

    elif 'logged-in' in session:
      if 'edit' in session:
        session.pop('edit', None)
        
      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 4, type='user')
      return render_template('dashboard/signup.html', data=vdict)
    
    elif self.userdb.select(1):
      return redirect('/login/')

    else:
      return render_template('dashboard/signup.html', data=vdict)

  def delete(self, id):
    author = session['logged-in']
    author_role = self.userdb.check_author(author)
    if author_role[3] == 'Admin':
      self.userdb.delete(id)

    return redirect('/dashboard/signup/')

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'កែតំរូវ​អ្នក​ប្រើប្រាស់'

    if 'logged-in' in session:
      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 4, type='user')
      vdict['user'] = self.userdb.select(id=id)
      date = (vdict['user'][5]).strftime('%d/%m/%Y')
      time = (vdict['user'][6]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)

      return render_template('dashboard/signup.html', data=vdict)

    return render_template('login.html', data=vdict)

  def load(self, page):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      vdict['users'] = self.userdb.select(vdict['dashboard_max_post'], page=page)
      vdict['thumbs'] = self.lib.get_thumbs(vdict['users'], 4, type="user")

      new_list = []
      for user in vdict['users']:
        new_user = list(user)
        new_user[5] = user[5].strftime('%d/%m/%Y') 
        new_user[6] = user[6].strftime('%H:%M:%S') 
        new_list.append(new_user)

      vdict['users'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)