#models/dashboard/postdb.py
import os, psycopg2

class Postdb():
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
    
    SQL = '''CREATE TABLE IF NOT EXISTS POSTS(
      ID TEXT,
      TITLE TEXT,
      CATEGORY VARCHAR(320),
      CONTENT TEXT,
      CATDATE DATE,
      CATTIME TIME,
      AUTHOR TEXT,
      VIDEO TEXT
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *post):
    self.set_conection()

    self.cursor.execute("INSERT INTO POSTS (ID, TITLE, CATEGORY, CONTENT, CATDATE, CATTIME, AUTHOR, VIDEO) VALUES %s ", (post,))
  
    self.conn.commit()
    self.conn.close()

  def update(self, *post):
    self.set_conection()

    sql = "UPDATE POSTS SET ID = %s, TITLE = %s, CATEGORY = %s, CONTENT = %s, CATDATE = %s, CATTIME = %s, AUTHOR = %s, VIDEO = %s WHERE ID = '"+post[0]+"'"
    self.cursor.execute(sql, post)

    self.conn.commit()
    self.conn.close()

  def select(self, amount=0, id=0, category='', page=0):
    self.set_conection()
    
    if category:
      SQL = "SELECT * FROM POSTS WHERE CATEGORY = %s ORDER BY CATDATE DESC, CATTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (category, amount*page, amount))
      result = self.cursor.fetchall()
    elif id:
      SQL = "SELECT * FROM POSTS WHERE ID = %s LIMIT 1"
      self.cursor.execute(SQL, (id,))
      result = self.cursor.fetchone()
    elif page:
      SQL = "SELECT * FROM POSTS ORDER BY CATDATE DESC, CATTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    else:
      SQL = "SELECT * FROM POSTS ORDER BY CATDATE DESC, CATTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()
    
    self.conn.close()
    return result

  def delete(self, id):
    self.set_conection()

    SQL = "DELETE FROM POSTS WHERE ID = %s"
    self.cursor.execute(SQL, (id,))

    self.conn.commit()
    self.conn.close()

  def search(self, query):
    self.set_conection()
  
    sql = "SELECT * from POSTS WHERE"
    sql += " TITLE LIKE '%"+query+"%'"
    sql += " OR CONTENT LIKE '%"+query+"%'"
    sql += " ORDER BY CATDATE DESC, CATTIME DESC LIMIT 20"

    self.cursor.execute(sql)
    
    result = self.cursor.fetchall()
    return result