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
    vdict['categories'] = self.categorydb.select(vdict['dashboard_max_category'])
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
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
      except ValueError:
        vdict['message'] = 'ទំរង់​កាលបរិច្ឆេទ​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/category.html', data=vdict)

      try:
        time = datetime.datetime.strptime(time, "%H:%M:%S")
      except ValueError:
        vdict['message'] = 'ទំរង់​ពេល​វេលា​មិន​ត្រឹមត្រូវ!'
        return render_template('dashboard/category.html', data=vdict)

      self.categorydb.insert(category, content, date, time, author)
      vdict['categories'] = self.categorydb.select(vdict['dashboard_max_category'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['categories'], 2)

      return render_template('dashboard/category.html', data=vdict)

    else:
      if 'logged-in' in session:
        return render_template('dashboard/category.html', data=vdict)

      return render_template('login.html', data=vdict)

  def delete(self, category):
    if 'logged-in' in session:
      self.categorydb.delete(category)
      return redirect('/dashboard/category/')

    return render_template('login.html', data=vdict)

  def edit(self, category):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      vdict['blog_title'] = 'បង្កើតប្រភេទមេរៀន'
      vdict['categories'] = self.categorydb.select(vdict['dashboard_max_category'])
      vdict['thumbs'] = self.lib.get_thumbs(vdict['categories'], 2)
      category = self.categorydb.select(1, category)
      vdict['datetime'] = (category[3].strftime('%d/%m/%Y'), category[4].strftime('%H:%M:%S'))
      vdict['category'] = category

      return render_template('dashboard/category.html', data=vdict)

    return render_template('login.html', data=vdict)

  def load(self, page):
    if 'logged-in' in session:
      vdict = copy.deepcopy(config.vdict)
      vdict['blog_title'] = 'បង្កើតប្រភេទមេរៀន'
      vdict['categories'] = self.categorydb.select(vdict['dashboard_max_category'], page=page)
      vdict['thumbs'] = self.lib.get_thumbs(vdict['categories'], 2)
      new_list = []
      for category in vdict['categories']:
        new_cat = list(category)
        new_cat[3] = category[3].strftime('%d/%m/%Y') 
        new_cat[4] = category[4].strftime('%H:%M:%S') 
        new_list.append(new_cat)

      vdict['categories'] = new_list
      return vdict
    else:
      return render_template('login.html', data=vdict)