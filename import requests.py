import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    for item in soup.select('.product'):  # Asegúrate de usar el selector correcto para los productos
        name = item.select_one('.product-name').text
        price = item.select_one('.product-price').text
        availability = item.select_one('.product-availability').text
        products.append({
            'name': name.strip(),
            'price': price.strip(),
            'availability': availability.strip()
        })
    return products

url = 'http://example.com/products'
html = get_html(url)
if html:
    products = parse_html(html)
    for product in products:
        print(product)
