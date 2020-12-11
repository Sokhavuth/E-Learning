#models/dashboard/bookdb.py
import os, psycopg2

class Bookdb():
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
    
    SQL = '''CREATE TABLE IF NOT EXISTS BOOKS(
      ID TEXT,
      TITLE TEXT,
      CONTENT TEXT,
      CATDATE DATE,
      CATTIME TIME,
      AUTHOR TEXT
    )'''

    self.cursor.execute(SQL)
    self.conn.commit()
    self.conn.close() 

  def insert(self, *book):
    self.set_conection()

    self.cursor.execute("INSERT INTO BOOKS (ID, TITLE, CONTENT, CATDATE, CATTIME, AUTHOR) VALUES %s ", (book,))
  
    self.conn.commit()
    self.conn.close()

  def update(self, *book):
    self.set_conection()

    sql = "UPDATE BOOKS SET ID = %s, TITLE = %s, CONTENT = %s, CATDATE = %s, CATTIME = %s, AUTHOR = %s WHERE ID = '"+book[0]+"'"
    self.cursor.execute(sql, book)

    self.conn.commit()
    self.conn.close()

  def select(self, amount=0, id=0, page=0):
    self.set_conection()
    
    if id:
      SQL = "SELECT * FROM BOOKS WHERE ID = %s LIMIT 1"
      self.cursor.execute(SQL, (id,))
      result = self.cursor.fetchone()
    elif page:
      SQL = "SELECT * FROM BOOKS ORDER BY CATDATE DESC, CATTIME DESC OFFSET %s ROWS FETCH NEXT %s ROWS ONLY"
      self.cursor.execute(SQL, (amount*page, amount))
      result = self.cursor.fetchall()
    else:
      SQL = "SELECT * FROM BOOKS ORDER BY CATDATE DESC, CATTIME DESC LIMIT %s"
      self.cursor.execute(SQL, (amount,))
      result = self.cursor.fetchall()
    
    self.conn.close()
    return result

  def delete(self, id):
    self.set_conection()

    SQL = "DELETE FROM BOOKS WHERE ID = %s"
    self.cursor.execute(SQL, (id,))

    self.conn.commit()
    self.conn.close()

  def search(self, query):
    self.set_conection()
  
    sql = "SELECT * from BOOKS WHERE"
    sql += " TITLE LIKE '%"+query+"%'"
    sql += " OR CONTENT LIKE '%"+query+"%'"
    sql += " ORDER BY CATDATE DESC, CATTIME DESC LIMIT 20"

    self.cursor.execute(sql)
    
    result = self.cursor.fetchall()
    return result