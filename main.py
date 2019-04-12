from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("http://www.scholarscup.org/calendar/")

soup = BeautifulSoup(page.content, 'html.parser')

events = soup.findAll("div", {"class": "event"})

names = []
dates = []

for event in events:
    details = event.find("div", {"class": "span5"})

    name = [elem.find("a").text for elem in details.findAll("h3")][0].encode().strip()
    
    date = event.find("div", {"class": "date"}).text.encode().strip()

    names.append(name)
    dates.append(date)

print(names)
print(dates)

with open('sitecal.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for n, d in zip(names, dates):
        writer.writerow([n, d])
