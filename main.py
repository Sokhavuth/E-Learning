#main.py
import os
from controllers.index import Index
     
app = Index()
     
if 'DYNO' in os.environ:
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 9000))
else: 
  app.run(host='localhost', port=9000, debug=True, reloader=True)