#models/userdb.py
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

    self.cursor.execute("INSERT INTO CATEGORIES (CATEGORY, CONTENT, CATDATE, CATTIME, AUTHOR) VALUES %s ", (category,))
  
    self.conn.commit()
    self.conn.close()

  def select(self, amount):
    self.set_conection()

    SQL = "SELECT * FROM CATEGORIES LIMIT %s"
    self.cursor.execute(SQL, (amount,))
    result = self.cursor.fetchall()
    
    self.conn.close()
    return result