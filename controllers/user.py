#controllers/user.py
import config, copy
from flask import render_template
from models.userdb import Userdb

class User():
  def __init__(self):
    self.userdb = Userdb()
  
  def get_user(self, id):
    vdict = copy.deepcopy(config.vdict)
    vdict['user'] = self.userdb.select(1, id=id)

    return vdict