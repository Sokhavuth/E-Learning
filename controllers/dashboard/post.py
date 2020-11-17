#controllers/dashboard/post.py
import config, copy, uuid, datetime
from flask import render_template, session, redirect, request
from lib import Lib
from models.dashboard.postdb import Postdb
from models.dashboard.categorydb import Categorydb

class Post():
  def __init__(self):
    self.lib = Lib()
    self.postdb = Postdb()
    self.category = Categorydb()

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ចុះ​ផ្សាយមេរៀន'
    vdict['datetime'] = self.lib.get_timezone()
    vdict['categories'] = self.category.select('all')

    if (request.method == "POST") and ('logged-in' in session):
      title = request.form['fpost-title']
      if not title:
        title = 'unknown'
        
      category = request.form['fcategory']
      content = request.form['fcontent']
      date = request.form['fpost-date']
      time = request.form['fpost-time']
      author = session['logged-in']

      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/dashboard.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/dashboard.html', data=vdict)

      id = str(uuid.uuid4().int)
      if 'edit' in session:
        self.postdb.update(session['edit'], title, category, content, date, time, author)
        session.pop('edit', None)
      else:
        self.postdb.insert(id, title, category, content, date, time, author)

      vdict['posts'] = self.postdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['posts'], 3)

      return render_template('dashboard/dashboard.html', data=vdict)

    elif 'logged-in' in session:
      vdict['posts'] = self.postdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['posts'], 3)
      return render_template('dashboard/dashboard.html', data=vdict)
    else:
      return redirect('/login/')

  def delete(self, id):
    if 'logged-in' in session:
      self.postdb.delete(id)
      return redirect('/dashboard/')

    return render_template('login.html', data=vdict)

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'កែតំរូវ​មេរៀន'

    if 'logged-in' in session:
      vdict['posts'] = self.postdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['posts'], 3)
      vdict['post'] = self.postdb.select(id=id)
      date = (vdict['post'][4]).strftime('%d/%m/%Y')
      time = (vdict['post'][5]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)
      vdict['categories'] = self.category.select('all')

      return render_template('/dashboard/dashboard.html', data=vdict)

    return render_template('login.html', data=vdict)