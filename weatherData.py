import requests
from bs4 import BeautifulSoup


from datetime import datetime

day = datetime.today().strftime('%Y%m%d')

# REPLACE THESE WITH YOUR OWN.
# DEFAULTS ARE NYC
lat = '40.758896'
long = '-73.985130'

page = requests.get("https://forecast.weather.gov/MapClick.php?lon=" + long + "&lat=" + lat)

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = (week.find_all(class_='tombstone-container'))
curent_cond = soup.find(id='current-conditions-body')
cur_temp = curent_cond.find(class_='myforecast-current-lrg').get_text()
cur_forecast = curent_cond.find(class_="myforecast-current").get_text()


info = {'day': day,
        'condition': cur_forecast,
        'temp': cur_temp, }

for entry in info:
    print(info[entry])
