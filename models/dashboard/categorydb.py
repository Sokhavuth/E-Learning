#models/dashboard/categorydb.py
import os, psycopg2

class Categorydb():
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
    
    SQL = '''CREATE TABLE IF NOT EXISTS CATEGORIES(
      ID SERIAL PRIMARY KEY,
      CATEGORY VARCHAR(320),
      CONTENT TEXT,
      CATDATE DATE,
      CATTIME TIME,
      AUTHOR VARCHAR(320)
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *category):
    self.set_conection()

    self.cursor.execute("SELECT CATEGORY FROM CATEGORIES WHERE CATEGORY = %s", (category[0],))
    result = self.cursor.fetchone()
    if not result:
      self.cursor.execute("INSERT INTO CATEGORIES (CATEGORY, CONTENT, CATDATE, CATTIME, AUTHOR) VALUES %s ", (category,))
    else:
      sql = "UPDATE CATEGORIES SET CATEGORY = %s, CONTENT = %s, CATDATE = %s, CATTIME = %s, AUTHOR = %s WHERE CATEGORY = '"+category[0]+"'"
      self.cursor.execute(sql, category)
  
    self.conn.commit()
    self.conn.close()

  def select(self, amount, category='', page=0):
    self.set_conection()

    if category:
      SQL = "SELECT * FROM CATEGORIES WHERE CATEGORY = %s LIMIT 1"
      self.cursor.execute(SQL, (category,))
      result = self.cursor.fetchone()
    elif page:
      SQL = "SELECT * FROM CATEGORIES ORDER BY CATDATE DESC, CATTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    elif amount == 'all':
      SQL = "SELECT * FROM CATEGORIES ORDER BY CATDATE DESC, CATTIME DESC"
      self.cursor.execute(SQL)
      result = self.cursor.fetchall()
    else:
      SQL = "SELECT * FROM CATEGORIES ORDER BY CATDATE DESC, CATTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()
    
    self.conn.close()
    return result

  def delete(self, category):
    self.set_conection()

    SQL = "DELETE FROM CATEGORIES WHERE CATEGORY = %s"

    self.cursor.execute(SQL, (category,))

    self.conn.commit()
    self.conn.close()