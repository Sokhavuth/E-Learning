#models/userdb.py
import os, psycopg2

class Userdb():
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
    self.set_conection()

    self.cursor.execute("INSERT INTO TEACHERS (EMAIL, PASSWORD, ROLE) VALUES %s ", (user,))
  
    self.conn.commit()
    self.conn.close()

  def select(self, amount):
    self.set_conection()

  def check_user(self, *user):
    self.set_conection()

    SQL = "SELECT EMAIL, PASSWORD FROM TEACHERS WHERE EMAIL = %s AND PASSWORD = %s LIMIT 1"
    self.cursor.execute(SQL, user)
    result = self.cursor.fetchone()
    
    self.conn.close()
    return result