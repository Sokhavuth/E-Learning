#models/userdb.py
import os, psycopg2

class Userdb():
  def __init__(self):
    self.createTable()

  def setConection(self):
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

  def createTable(self):
    self.setConection()
    
    SQL = '''CREATE TABLE IF NOT EXISTS TEACHERS(
      ID SERIAL PRIMARY KEY,
      EMAIL VARCHAR(320),
      PASSWORD VARCHAR(320),
      ROLE TEXT
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *user):
    self.setConection()

    self.cursor.execute("INSERT INTO TEACHERS (EMAIL, PASSWORD, ROLE) VALUES %s ", (user,))
  
    self.conn.commit()
    self.conn.close()