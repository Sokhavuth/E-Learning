#controllers/post.py
import config, copy
from flask import render_template
from models.dashboard.pagedb import Pagedb

class Page():
  def __init__(self):
    self.pagedb = Pagedb()
  
  def get_page(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['page'] = self.pagedb.select(1, id=id)

    return vdict