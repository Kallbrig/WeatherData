import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

from datetime import datetime

day = datetime.today().strftime('%Y%m%d')

page = requests.get("https://forecast.weather.gov/MapClick.php?lon=-85.96042156219481&lat=31.78950142221656")

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = (week.find_all(class_='tombstone-container'))
curent_cond = soup.find(id='current-conditions-body')

cur_temp = curent_cond.find(class_='myforecast-current-lrg').get_text()
cur_forecast = curent_cond.find(class_="myforecast-current").get_text()
print(cur_temp)
print(cur_forecast)

line = {'day': day,
        'condition': cur_forecast,
        'temp': cur_temp, }

print(line)
