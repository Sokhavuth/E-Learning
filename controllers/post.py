#controllers/post.py
import config, copy
from flask import render_template, redirect
from lib import Lib
from models.dashboard.postdb import Postdb

class Post():
  def __init__(self):
    self.postdb = Postdb()
    self.lib = Lib()

  def get_post(self, amount=5, category="", page=0):
    vdict = copy.deepcopy(config.vdict)
    vdict['posts'] = self.postdb.select(amount=amount, category=category, page=page)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['posts'], 3)
    vdict['videos'] = self.lib.get_video_data(vdict['posts'], 7)
    vdict['category'] = category

    new_post_list = []
    for post in vdict['posts']:
      new_post = list(post)
      new_post[4] = post[4].strftime('%d/%m/%Y') 
      new_post[5] = post[5].strftime('%H:%M:%S') 
      new_post_list.append(new_post)

    vdict['posts'] = new_post_list

    return vdict

  def get_single_post(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['post'] = self.postdb.select(1, id=id)

    return vdict