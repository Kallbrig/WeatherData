import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lon=-85.96042156219481&lat=31.78950142221656")

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = (week.find_all(class_='tombstone-container'))

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_desc': short_desc,
        'temp': temp,
    }
)

print(weather_stuff)

weather_stuff.to_csv('result.csv')
