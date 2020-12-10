#models/dashboard/settingdb.py
import os, psycopg2

class Settingdb():
  def __init__(self):
    self.create_table()

  def set_conection(self):
    if 'DYNO' in os.environ:
      DATABASE_URL = os.environ['DATABASE_URL']
      self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
      self.cursor = self.conn.cursor()
    else: 
      self.conn = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="sokhavuth", 
        host="localhost", 
        port="5432"
      )

      self.cursor = self.conn.cursor()

  def create_table(self):
    self.set_conection()
    
    SQL = '''CREATE TABLE IF NOT EXISTS SETTING(
      dashboard_max_post int,
      dashboard_max_category int,
      post_max_category int,
      book_max_post int,
      blog_title text,
      blog_description text,
      secret_key text
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *setting):
    self.set_conection()

    SQL = '''INSERT INTO SETTING 
    (dashboard_max_post, dashboard_max_category, post_max_category, book_max_post, blog_title, blog_description, secret_key) VALUES %s 
    '''
    self.cursor.execute(SQL, (setting,))
  
    self.conn.commit()
    self.conn.close()

  def update(self, *setting):
    self.set_conection()

    sql = '''UPDATE SETTING SET dashboard_max_post = %s, 
    dashboard_max_category = %s, 
    post_max_category = %s, 
    book_max_post = %s, 
    blog_title = %s, 
    blog_description = %s,
    secret_key = %s
    '''
    self.cursor.execute(sql, setting)

    self.conn.commit()
    self.conn.close()

  def select(self):
    self.set_conection()
    
    SQL = "SELECT * FROM SETTING LIMIT 1"
    self.cursor.execute(SQL)
    result = self.cursor.fetchone()
    
    self.conn.close()
    return result