from api_directory.api_classes.api_cls import Book

import requests
from bs4 import BeautifulSoup


def get_page(page_number):
    try:
        response = requests.get(f'https://books.toscrape.com/catalogue/page-{page_number}.html')
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
        lstEl.append(Book(title=title, price=price, rating=rating))
    if len(lstEl) == 0:
        return None
    return lstEl

def orchestrator(page_number=1):
    page = get_page(page_number)
    return soup_page(page)

