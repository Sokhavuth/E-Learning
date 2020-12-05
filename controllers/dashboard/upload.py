#controllers/dashboard/upload.py
import os, config, copy, uuid
from flask import render_template, request, session
from werkzeug.utils import secure_filename

class Upload():
  def __init__(self):
    pass

  def get_post(self):
    vdict = copy.deepcopy(config.vdict)

    if (request.method == "POST") and ('logged-in' in session):
      f = request.files['fupload']
      if f != '':
        id = str(uuid.uuid4().int)
        url = '/static/uploads/' + id + '_' + secure_filename(f.filename)
        ROOT_DIR = os.path.dirname(os.path.abspath("config.py"))
        savePath = ROOT_DIR + url
        f.save(savePath)
        vdict['url'] = url
        return render_template('dashboard/uploadurl.html', data=vdict)
      else:
        return render_template('dashboard/upload.html', data=vdict)
      
    else:
      return render_template('dashboard/upload.html', data=vdict)