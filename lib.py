#lib.py
from pytz import timezone
from datetime import datetime 

class Lib():
  def __init__(self):
    pass

  def get_timezone(self):
    khtz = timezone('Asia/Phnom_Penh')
    date = datetime.now().astimezone(tz=khtz).strftime('%d-%m-%Y')
    time = datetime.now().astimezone(tz=khtz).strftime('%H:%M:%S')
    return (date, time)