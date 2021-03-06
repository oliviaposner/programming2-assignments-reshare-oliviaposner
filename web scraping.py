# PROBLEM 1 (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/kimkardashian"
page = requests.get(url)



soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

tweets = soup.findAll("p", class_="tweet-text")
tweets = [x.text.strip() for x in tweets]

for i in range(5):
    print("\n")
    print(tweets)


# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

url = "https://weather.com/weather/tenday/l/Chicago+IL+USIL0225:1:US"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

temperature = soup.findAll("td", class_="temp")
temperature = [x.text.strip() for x in temperature]

description = soup.findAll("td", class_="description")
description = [x.text.strip() for x in description]

day_date = soup.findAll("span", class_="day-detail")
day_date = [x.text.strip() for x in day_date]

rain = soup.findAll("td", class_="precip")
rain = [x.text.strip() for x in rain]

wind = soup.findAll("td", class_="wind")
wind = [x.text.strip() for x in wind]

humidity = soup.findAll("td", class_="humidity")
humidity = [x.text.strip() for x in humidity]


for i in range(len(wind)):
    print("\n")
    print(day_date[i], "will be", description[i], "with a high/low temperature of", temperature[i],", humidity at", humidity[i], ". There is a", rain[i], "chance of rain with winds out of the WNW at", wind[i],".")