from scraper.fetcher import get_html
from scraper.parser import parse_html
from analysis.analyzer import analyze_data, save_to_csv
from utils.decorators import log_execution

@log_execution
def fetch_and_analyze(url):
    html = get_html(url)
    if html:
        data = parse_html(html)
        df = analyze_data(data)
        save_to_csv(df, 'products.csv')
        return df
    return None

# Llamada a la función principal
url = 'http://example.com/products'
fetch_and_analyze(url)
