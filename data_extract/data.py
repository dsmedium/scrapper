import requests
from bs4 import BeautifulSoup

all_prices = []


def get_prices(url):

    # get the source code of the page
    result = requests.get(url)
    src = result.content

    # parse the source code
    soup = BeautifulSoup(src,'lxml')

    # find all the classes containing prices
    price = soup.find_all("span", {"class": "per-sale-price price-main"})
    for value in price:
        text = value.text
        a = text.strip().lstrip("$")
        all_prices.append(float(a))


def second_highest():

    # sorting prices
    all_prices.sort()
    return all_prices[-1]
