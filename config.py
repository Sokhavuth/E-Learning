#config.py
from models.dashboard.settingdb import Settingdb

vdict = {}
vdict['message'] = ''
vdict['page'] = 0

settingdb = Settingdb()
setting = settingdb.select()

if not setting:
  vdict['dashboard_max_post'] = 5
  vdict['dashboard_max_category'] = 5
  vdict['post_max_category'] = 20
  vdict['book_max_post'] = 8
  vdict['blog_title'] = "សាលារៀនពីចំងាយ"
  vdict['blog_description'] = "ចេះ​ពី​រៀន​ មាន​ពី​រក"
  vdict['secret_key'] = 'c89f675a9b7c74ffca5a44a0cf3e3acc'

  settingdb.insert(vdict['dashboard_max_post'], vdict['dashboard_max_category'], vdict['post_max_category'], vdict['book_max_post'], vdict['blog_title'], vdict['blog_description'], vdict['secret_key'])
else:
  vdict['dashboard_max_post'] = setting[0]
  vdict['dashboard_max_category'] = setting[1]
  vdict['post_max_category'] = setting[2]
  vdict['book_max_post'] = setting[3]
  vdict['blog_title'] = setting[4]
  vdict['blog_description'] = setting[5] 
  vdict['secret_key'] = setting[6] 