#controllers/dashboard/setting.py
import config, copy, uuid, datetime, importlib
from flask import render_template, session, redirect, request
from lib import Lib
from models.dashboard.settingdb import Settingdb

class Setting():
  def __init__(self):
    self.lib = Lib()
    self.settingdb = Settingdb()

  def get_set(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'កំណត់​ទំរង់​លក្ខណៈ'

    if (request.method == "POST") and ('logged-in' in session):

      max_post = request.form['fmax-post']
      max_category = request.form['fmax-category']
      max_post_category = request.form['fmax-post-category']
      max_book = request.form['fbook-post']
      blog_title = request.form['fblog-title']
      blog_description = request.form['fblog-description']
      secret_key = request.form['fsecret-key']

      if self.settingdb.select():
        self.settingdb.update(max_post, max_category, max_post_category, max_book, blog_title, blog_description, secret_key)
      else:
        self.settingdb.insert(max_post, max_category, max_post_category, max_book, blog_title, blog_description, secret_key)

      importlib.reload(config)
      vdict['setting'] = self.settingdb.select()

      return render_template('dashboard/setting.html', data=vdict)

    elif 'logged-in' in session:
      setting = self.settingdb.select()
      if setting:
        vdict['setting'] = setting

      return render_template('dashboard/setting.html', data=vdict)
    else:
      return redirect('/login/')