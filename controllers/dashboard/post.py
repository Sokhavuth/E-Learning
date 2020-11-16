#controllers/dashboard/post.py
import config, copy
from flask import render_template, session, redirect
from lib import Lib
from models.dashboard.postdb import Postdb
from models.dashboard.categorydb import Categorydb

class Post():
  def __init__(self):
    self.lib = Lib()
    self.post = Postdb()
    self.category = Categorydb()

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ចុះ​ផ្សាយមេរៀន'
    vdict['datetime'] = self.lib.get_timezone()
    vdict['categories'] = self.category.select('all')

    if 'logged-in' in session:
      return render_template('dashboard/dashboard.html', data=vdict)
    else:
      return redirect('/login/')