#controllers/dashboard/search.py
import config, copy
from flask import render_template, session, redirect, request
from lib import Lib
from models.dashboard.postdb import Postdb
from models.dashboard.categorydb import Categorydb
from models.dashboard.pagedb import Pagedb
from models.dashboard.bookdb import Bookdb
from models.userdb import Userdb
from models.dashboard.settingdb import Settingdb

class Search():
  def __init__(self):
    self.lib = Lib()
    self.postdb = Postdb()
    self.categorydb = Categorydb()
    self.pagedb = Pagedb()
    self.bookdb = Bookdb()
    self.userdb = Userdb()
    self.settingdb = Settingdb()

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ទំព័រ​ស្វែង​រក'

    if (request.method == "POST") and ('logged-in' in session):
      database = request.form['fsearch-option']
      fquery = request.form['fquery']

      if database == 'មេរៀន':
        vdict['search'] = self.postdb.search(fquery)
        vdict['type'] = 'post'
      elif database == 'ទំព័រ​មាតិកា':
        vdict['search'] = self.pagedb.search(fquery)
        vdict['type'] = 'page'
      elif database == 'សៀវភៅ':
        vdict['search'] = self.bookdb.search(fquery)
        vdict['type'] = 'book'

      return render_template('search.html', data=vdict)

    elif 'logged-in' in session:
      return render_template('search.html', data=vdict)
    else:
      return redirect('/login/')