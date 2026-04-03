import json
import requests
from bs4 import BeautifulSoup

def get_page():
    try:
        response = requests.get('https://books.toscrape.com/')
        response.raise_for_status()
        return response.text
    except Exception:
        return None

def soup_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    elements = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    lstEl = []
    for element in elements:
        title = element.h3.find('a').get('title')
        price = element.find('p', class_ = 'price_color').text
        rating = element.p.get('class')[1]
        lstEl.append({'title': title, 'price': price, 'rating': rating})
    if len(lstEl) == 0:
        return None
    return lstEl[:5]

def orchestrator():
    page = get_page()
    if page is None:
        return None
    return soup_page(page)