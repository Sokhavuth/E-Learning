#controllers/index.py
import config, copy, json
from flask import render_template, redirect, session, request
from flask_classful import FlaskView, route
from controllers.post import Post
from controllers.page import Page
from controllers.book import Book
from controllers.user import User
from controllers.search import Search

class Index(FlaskView):
    def __init__(self):
        self.post = Post()
        self.page = Page()
        self.book = Book()
        self.user = User()
        self.search = Search()

    @route('/')
    def index(self):
        session['page'] = 0
        vdict = self.post.get_post()
        vdict['books'] = self.book.get_post_book()
        return render_template('index.html', data=vdict)

    @route('/panel')
    def get_post(self):
        nav = request.args.get('nav', 0, type=str)

        if nav == 'previous':
            session['page'] += 1
        elif nav == 'next':
            if session['page'] > 0:
                session['page'] -= 1
        else:
            session['page'] = 0

        vdict = self.post.get_post(page=session['page'])
        
        if not vdict['posts']:
            session['page'] -= 1

        return json.dumps(vdict)

    @route('/favicon.ico')
    def favicon(self):
        redirect('/static/images/site_logo.png')

    @route('/post/<id>')
    def get_single_post(self, id):
        vdict = self.post.get_single_post(id)
        return render_template('post.html', data=vdict)

    @route('/post/load/<label>')
    def load_post(self, label):
        vdict = self.post.get_post(config.vdict['post_max_category'], category=label)
        return vdict

    @route('/post/load/ajax/<label>')
    def load_post(self, label):
        ajax = request.args.get('ajax', 0, type=int)
        
        vdict = self.post.get_post(config.vdict['post_max_category'], category=label, page=ajax)
        return vdict

    @route('/category/<label>')
    def get_post_category(self, label):
        vdict = self.post.get_post(config.vdict['post_max_category'], category=label)
        return render_template('category.html', data=vdict)

    @route('/page/<id>')
    def get_post_page(self, id):
        vdict = self.page.get_page(id)
        return render_template('page.html', data=vdict)

    @route('/book/load/')
    def load_book(self):
        ajax = request.args.get('ajax', 0, type=int)
        return self.book.load(page=ajax)

    @route('/book/<id>')
    def get_post_book(self, id):
        vdict = self.book.get_book(id)
        return render_template('book.html', data=vdict)

    @route('/user/<id>')
    def get_user(self, id):
        vdict = self.user.get_user(id)
        return render_template('user.html', data=vdict)

    @route('/search/', methods=['GET', 'POST'])
    def get_post_search(self):
        return self.search.get_post()