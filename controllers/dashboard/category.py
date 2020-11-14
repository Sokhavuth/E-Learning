#controllers/dashboard/category.py
import config, copy, lib, datetime
from flask import render_template, request, session, redirect
from models.dashboard.categorydb import Categorydb

class Category():
  def __init__(self):
    self.categorydb = Categorydb()
    self.lib = lib.Lib()

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'បង្កើតប្រភេទមេរៀន'
    vdict['datetime'] = self.lib.get_timezone()
    vdict['categories'] = self.categorydb.select(5)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['categories'], 2)

    if (request.method == "POST") and ('logged-in' in session):
      category = request.form['fcategory-title']
      if not category:
        category = 'unknown'
        
      content = request.form['fcontent']
      date = request.form['fcategory-date']
      time = request.form['fcategory-time']
      author = session['logged-in']

      try:
        date = datetime.datetime.strptime(date, "%d-%m-%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/category.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/category.html', data=vdict)

      self.categorydb.insert(category, content, date, time, author)
      vdict['categories'] = self.categorydb.select(5)
      vdict['thumbs'] = self.lib.get_thumbs(vdict['categories'], 2)

      return render_template('dashboard/category.html', data=vdict)

    else:
      if 'logged-in' in session:
        return render_template('dashboard/category.html', data=vdict)

      return render_template('login.html', data=vdict)
