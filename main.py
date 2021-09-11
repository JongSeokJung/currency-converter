import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from country_list import display, get_country

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""


def prompt():
    print("Where are you from? Choose a country by number.")
    while True:
        try:
            user_input = input("#:")
            first_country = get_country(int(user_input))
            print(f"{first_country['name']}")
            break
        except IndexError:
            print("Choose a number from the list.")
        except ValueError:
            print("That wasn't a number.")

    while True:
        try:
            print("Now Choose another country.")
            user_input = input("#: ")
            second_country = get_country(int(user_input))
            print(f"{second_country['name']}")
            break
        except IndexError:
            print("Choose a number from the list.")
        except ValueError:
            print("That wasn't a number.")

    url = f"https://wise.com/gb/currency-converter/{first_country['code']}-to-{second_country['code']}-rate?amount=1"
    ratio = get_ratio(url)
    convert(first_country['code'], second_country['code'], ratio)


def convert(first_currency, second_currency, ratio):
    print(
        f"How many {first_currency} do you want to convert to {second_currency}?")
    while True:
        try:
            amount = int(input())
            break
        except ValueError:
            print("That wasn't a number.")

    first = format_currency(amount, first_currency, locale="ko_KR")
    second = format_currency(amount*ratio, second_currency, locale="ko_KR")
    print(f"{first} is {second}")


def get_ratio(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    ratio = soup.find("h3", {"class": "cc__source-to-target"}
                      ).find("span", {"class": "text-success"}).text
    return float(ratio)


display()
prompt()
