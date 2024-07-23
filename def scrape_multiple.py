def scrape_multiple_pages(base_url, pages):
    all_products = []
    for page in range(1, pages + 1):
        url = f'{base_url}?page={page}'
        products = fetch_and_parse(url)
        if products:
            all_products.extend(products)
        else:
            print(f'Error fetching data from page {page}')
    return all_products

base_url = 'http://example.com/products'
all_products = scrape_multiple_pages(base_url, 5)
df = analyze_data(all_products)
save_to_csv(df, 'all_products.csv')
