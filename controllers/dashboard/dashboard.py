#controllers/dashboard/dashboard.py
from flask import session, render_template
from flask_classful import FlaskView, route
from controllers.dashboard.category import Category
from controllers.dashboard.post import Post
from controllers.dashboard.page import Page
from controllers.dashboard.book import Book
from controllers.dashboard.upload import Upload

class Dashboard(FlaskView):
  def __init__(self):
    self.cat = Category()
    self.post = Post()
    self.page = Page()
    self.book = Book()
    self.upload = Upload()

  @route('/', methods=['GET', 'POST'])
  def index(self):
    session['page'] = 0
    return self.post.get_post()

  @route('/category/', methods=['GET', 'POST'])
  def category(self):
    session['page'] = 0
    return self.cat.get_post()

  @route('/category/delete/<category>')
  def delete_category(self, category):
    return self.cat.delete(category)

  @route('/category/edit/<category>')
  def edit_category(self, category):
    return self.cat.edit(category)

  @route('/category/load/')
  def load_category(self):
    session['page'] += 1
    return self.cat.load(session['page'])

  @route('/post/delete/<id>')
  def delete_post(self, id):
    return self.post.delete(id)

  @route('/post/edit/<id>')
  def edit_post(self, id):
    session['edit'] = id
    return self.post.edit(id)

  @route('/post/load/')
  def load_post(self):
    session['page'] += 1
    return self.post.load(session['page'])

  @route('/page/', methods=['GET', 'POST'])
  def get_post_page(self):
    session['page'] = 0
    return self.page.get_post_page()

  @route('/page/edit/<id>')
  def edit_page(self, id):
    session['edit'] = id
    return self.page.edit(id)

  @route('/page/delete/<id>')
  def delete_page(self, id):
    return self.page.delete(id)

  @route('/page/load/')
  def load_page(self):
    session['page'] += 1
    return self.page.load(session['page'])

  @route('/book/', methods=['GET', 'POST'])
  def get_book(self):
    session['page'] = 0
    return self.book.get_post_book()

  @route('/book/edit/<id>')
  def edit_book(self, id):
    session['edit'] = id
    return self.book.edit(id)

  @route('/book/delete/<id>')
  def delete_book(self, id):
    return self.book.delete(id)

  @route('/book/load/')
  def load_book(self):
    session['page'] += 1
    return self.book.load(session['page'])

  @route('/upload/', methods=['GET', 'POST'])
  def upload_file(self):
    return self.upload.get_post()
    
 
dashboard = Dashboard()