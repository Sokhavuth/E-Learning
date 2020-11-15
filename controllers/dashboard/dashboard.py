#controllers/category.py
import config, copy
from flask import render_template, session, redirect
from flask_classful import FlaskView, route
from controllers.dashboard.category import Category

class Dashboard(FlaskView):
  def __init__(self):
    self.cat = Category()

  @route('/')
  def index(self):
    vdict = copy.deepcopy(config.vdict)
    vdict['blog_title'] = 'ទំព័រ​គ្រប់គ្រង'

    if 'logged-in' in session:
      return render_template('dashboard/dashboard.html', data=vdict)
    else:
      return redirect('/login/')

  @route('/category/', methods=['GET', 'POST'])
  def category(self):
    return self.cat.get_post()

  @route('/category/delete/<category>')
  def delete(self, category):
    return self.cat.delete(category)

  @route('/category/edit/<category>')
  def edit(self, category):
    return self.cat.edit(category)
    
dashboard = Dashboard()