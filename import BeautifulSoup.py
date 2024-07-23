from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    for item in soup.select('.product'):
        name = item.select_one('.product-name').text
        price = item.select_one('.product-price').text
        availability = item.select_one('.product-availability').text
        products.append({
            'name': name.strip(),
            'price': price.strip(),
            'availability': availability.strip()
        })
    return products
