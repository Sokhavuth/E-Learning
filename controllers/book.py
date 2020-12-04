#controllers/book.py
import config, copy, uuid, datetime
from flask import render_template, session, redirect, request
from lib import Lib
from models.dashboard.bookdb import Bookdb

class Book():
  def __init__(self):
    self.lib = Lib()
    self.bookdb = Bookdb()

  def get_post_book(self):
    vdict = copy.deepcopy(config.vdict)  
    vdict['books'] = self.bookdb.select(vdict['book_max_post'])
    vdict['thumbs'] = self.lib.get_thumbs(vdict['books'], 2)
    return vdict

  def get_book(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['book'] = self.bookdb.select(1, id=id)

    return vdict

  def load(self, page):
    vdict = copy.deepcopy(config.vdict)
    vdict['books'] = self.bookdb.select(vdict['book_max_post'], page=page)
    vdict['thumbs'] = self.lib.get_thumbs(vdict['books'], 2)

    new_list = []
    for book in vdict['books']:
      new_book = list(book)
      new_book[3] = book[3].strftime('%d/%m/%Y') 
      new_book[4] = book[4].strftime('%H:%M:%S') 
      new_list.append(new_book)

      vdict['books'] = new_list
      return vdict