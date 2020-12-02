#controllers/dashboard/post.py
import config, copy, uuid, datetime
from flask import render_template, session, redirect, request
from lib import Lib
from models.dashboard.pagedb import Pagedb

class Page():
  def __init__(self):
    self.lib = Lib()
    self.pagedb = Pagedb()

  def get_post_page(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'បង្កើត​ទំព័រ​មាតិកា'
    vdict['datetime'] = self.lib.get_timezone()

    if (request.method == "POST") and ('logged-in' in session):
      title = request.form['fpage-title']
      if not title:
        title = 'unknown'
        
      content = request.form['fcontent']
      date = request.form['fpage-date']
      time = request.form['fpage-time']
      author = session['logged-in']

      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/page.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/page.html', data=vdict)

      id = str(uuid.uuid4().int)
      if 'edit' in session:
        self.pagedb.update(session['edit'], title, content, date, time, author)
        session.pop('edit', None)
      else:
        self.pagedb.insert(id, title, content, date, time, author)

      vdict['pages'] = self.pagedb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['pages'], 2)

      return render_template('dashboard/page.html', data=vdict)

    elif 'logged-in' in session:
      if 'edit' in session:
        session.pop('edit', None)
        
      vdict['pages'] = self.pagedb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['pages'], 2)
      return render_template('dashboard/page.html', data=vdict)
    else:
      return redirect('/login/')

  def delete(self, id):
    if 'logged-in' in session:
      self.pagedb.delete(id)
      return redirect('/dashboard/page/')

    return render_template('login.html', data=vdict)

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'កែតំរូវ​មាតិកា'

    if 'logged-in' in session:
      vdict['pages'] = self.pagedb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['pages'], 2)
      vdict['page'] = self.pagedb.select(id=id)
      date = (vdict['page'][3]).strftime('%d/%m/%Y')
      time = (vdict['page'][4]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)

      return render_template('/dashboard/page.html', data=vdict)

    return render_template('login.html', data=vdict)

  def load(self, page):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      vdict['pages'] = self.pagedb.select(vdict['dashboard_max_post'], page=page)
      vdict['thumbs'] = self.lib.get_thumbs(vdict['pages'], 2)

      new_list = []
      for page in vdict['pages']:
        new_page = list(page)
        new_page[3] = page[3].strftime('%d/%m/%Y') 
        new_page[4] = page[4].strftime('%H:%M:%S') 
        new_list.append(new_page)

      vdict['pages'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)