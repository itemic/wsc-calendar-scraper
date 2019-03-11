from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.scholarscup.org/calendar/")

soup = BeautifulSoup(page.content, 'html.parser')

events = soup.findAll("div", {"class": "event"})

for event in events:
    details = event.find("div", {"class": "span5"})

    name = [elem.find("a").text for elem in details.findAll("h3")][0]
    date = event.find("div", {"class": "date"}).text.strip()

