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
    
    SQL = '''CREATE TABLE IF NOT EXISTS USERS(
      ID SERIAL PRIMARY KEY,
      EMAIL VARCHAR(320),
      PASSWORD VARCHAR(320),
      ROLE TEXT,
      CONTENT TEXT,
      CATDATE DATE,
      CATTIME TIME,
      AUTHOR TEXT
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *user):
    self.set_conection()

    self.cursor.execute("INSERT INTO USERS (EMAIL, PASSWORD, ROLE, CONTENT, CATDATE, CATTIME, AUTHOR) VALUES %s ", (user,))
  
    self.conn.commit()
    self.conn.close()

  def select(self, amount=5, id='', page=0):
    self.set_conection()

    if id:
      SQL = "SELECT * FROM USERS WHERE ID=%s"
      self.cursor.execute(SQL, (id,))
      result = self.cursor.fetchone()
    elif page:
      SQL = "SELECT * FROM USERS ORDER BY ID DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    else:
      SQL = "SELECT * FROM USERS ORDER BY ID DESC LIMIT %s"
      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()

    self.conn.close()
    return result

  def check_email(self, email):
    self.set_conection()

    SQL = "SELECT EMAIL, PASSWORD FROM USERS WHERE EMAIL = %s LIMIT 1"
    self.cursor.execute(SQL, (email,))
    result = self.cursor.fetchone()
    
    self.conn.close()
    return result

  def check_user(self, *user):
    self.set_conection()

    SQL = "SELECT EMAIL, PASSWORD FROM USERS WHERE EMAIL = %s AND PASSWORD = %s LIMIT 1"
    self.cursor.execute(SQL, (user))
    result = self.cursor.fetchone()
    
    self.conn.close()
    return result

  def check_author(self, email):
    self.set_conection()

    SQL = "SELECT * FROM USERS WHERE EMAIL = %s LIMIT 1"
    self.cursor.execute(SQL, (email,))
    result = self.cursor.fetchone()
    
    self.conn.close()
    return result

  def delete(self, id):
    self.set_conection()

    SQL = "DELETE FROM USERS WHERE ID = %s"
    self.cursor.execute(SQL, (id,))

    self.conn.commit()
    self.conn.close()

  def update(self, *user):
    self.set_conection()

    sql = "UPDATE USERS SET EMAIL = %s, PASSWORD = %s, ROLE = %s, CONTENT = %s, CATDATE = %s, CATTIME = %s, AUTHOR = %s WHERE ID = %s"
    self.cursor.execute(sql, user)

    self.conn.commit()
    self.conn.close()

  def search(self, query):
    self.set_conection()
  
    sql = "SELECT * from USERS WHERE"
    sql += " EMAIL LIKE '%"+query+"%'"
    sql += " OR CONTENT LIKE '%"+query+"%'"
    sql += " ORDER BY CATDATE DESC, CATTIME DESC LIMIT 20"

    self.cursor.execute(sql)
    
    result = self.cursor.fetchall()
    return result