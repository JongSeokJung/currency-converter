import os
import requests
from bs4 import BeautifulSoup

os.system("clear")


url = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code = items[2].text
    if name and code:
        country = {
            'name': name.capitalize(),
            'code': code
        }
        countries.append(country)


def display():
    for index, country in enumerate(countries):
        print(f"#{index} {country['name']}")


def get_country(number):
    country = countries[number]
    return country
