#main.py
from flask import Flask
from controllers.index import Index

app = Flask(__name__)

Index.register(app, route_base='/')

if __name__ == '__main__':
  app.run(debug=True)