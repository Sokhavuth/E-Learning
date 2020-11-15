#lib.py
from pytz import timezone
from datetime import datetime 
from bs4 import BeautifulSoup

class Lib():
  def __init__(self):
    pass

  def get_timezone(self):
    khtz = timezone('Asia/Phnom_Penh')
    date = datetime.now().astimezone(tz=khtz).strftime('%d/%m/%Y')
    time = datetime.now().astimezone(tz=khtz).strftime('%H:%M:%S')
    return (date, time)

  def get_thumbs(self, items, index, type=None):
    item_contents = [BeautifulSoup(item[index], "html.parser") for item in items]
    
    images = []

    for item_content in item_contents:
      image = item_content.find('img')
      if not image:
        if type == "user":
          new_tag = item_content.new_tag('img', src="/static/images/userthumb.png")
        else:
          new_tag = item_content.new_tag('img', src="/static/images/no-image.png")

        images.append(new_tag)
      else:
        images.append(image)

    thumbs = []
    for image in images:
      src = (image['src']).split(' ')
      thumbs.append(src[0])

    return thumbs