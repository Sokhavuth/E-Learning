#main.py
import config
from flask import Flask
from controllers.index import Index
from controllers.login import Login
from controllers.dashboard.dashboard import Dashboard

app = Flask(__name__)
app.secret_key = config.vdict['secret_key']

Index.register(app, route_base='/')
Login.register(app, route_base='/login')
Dashboard.register(app, route_base='/dashboard')

if __name__ == '__main__':
  app.run(debug=True)