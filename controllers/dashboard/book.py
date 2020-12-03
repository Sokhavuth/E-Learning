#controllers/dashboard/post.py
import config, copy, uuid, datetime
from flask import render_template, session, redirect, request
from lib import Lib
from models.dashboard.bookdb import Bookdb

class Book():
  def __init__(self):
    self.lib = Lib()
    self.bookdb = Bookdb()

  def get_post_book(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ចុះផ្សាយ​សៀវភៅ'
    vdict['datetime'] = self.lib.get_timezone()

    if (request.method == "POST") and ('logged-in' in session):
      title = request.form['fbook-title']
      if not title:
        title = 'unknown'
        
      content = request.form['fcontent']
      date = request.form['fbook-date']
      time = request.form['fbook-time']
      author = session['logged-in']

      try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/book.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/book.html', data=vdict)

      id = str(uuid.uuid4().int)
      if 'edit' in session:
        self.bookdb.update(session['edit'], title, content, date, time, author)
        session.pop('edit', None)
      else:
        self.bookdb.insert(id, title, content, date, time, author)

      vdict['books'] = self.bookdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['books'], 2)
      
      return render_template('dashboard/book.html', data=vdict)

    elif 'logged-in' in session:
      if 'edit' in session:
        session.pop('edit', None)
        
      vdict['books'] = self.bookdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['books'], 2)
      return render_template('dashboard/book.html', data=vdict)
    else:
      return redirect('/login/')

  def delete(self, id):
    if 'logged-in' in session:
      self.bookdb.delete(id)
      return redirect('/dashboard/book/')

    return render_template('login.html', data=vdict)

  def edit(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'កែតំរូវ​សៀវភៅ'

    if 'logged-in' in session:
      vdict['books'] = self.bookdb.select(vdict['dashboard_max_post'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['books'], 2)
      vdict['book'] = self.bookdb.select(id=id)
      date = (vdict['book'][3]).strftime('%d/%m/%Y')
      time = (vdict['book'][4]).strftime('%H:%M:%S')
      vdict['datetime'] = (date, time)
      print(vdict['book'])
      return render_template('dashboard/book.html', data=vdict)

    return render_template('login.html', data=vdict)

  def load(self, page):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      vdict['books'] = self.bookdb.select(vdict['dashboard_max_post'], page=page)
      vdict['thumbs'] = self.lib.get_thumbs(vdict['books'], 2)

      new_list = []
      for book in vdict['books']:
        new_book = list(book)
        new_book[3] = book[3].strftime('%d/%m/%Y') 
        new_book[4] = book[4].strftime('%H:%M:%S') 
        new_list.append(new_book)

      vdict['books'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)