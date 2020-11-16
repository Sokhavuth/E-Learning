#controllers/dashboard/dashboard.py
from flask import session
from flask_classful import FlaskView, route
from controllers.dashboard.category import Category
from controllers.dashboard.post import Post

class Dashboard(FlaskView):
  def __init__(self):
    self.cat = Category()
    self.post = Post()

  @route('/', methods=['GET', 'POST'])
  def index(self):
    session['page'] = 0
    return self.post.get_post()

  @route('/category/', methods=['GET', 'POST'])
  def category(self):
    session['page'] = 0
    return self.cat.get_post()

  @route('/category/delete/<category>')
  def delete(self, category):
    return self.cat.delete(category)

  @route('/category/edit/<category>')
  def edit(self, category):
    return self.cat.edit(category)

  @route('/category/load/')
  def load(self):
    session['page'] += 1
    return self.cat.load(session['page'])
    
dashboard = Dashboard()