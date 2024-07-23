import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} executed in {end_time - start_time:.2f} seconds')
        return result
    return wrapper

@log_execution
def fetch_and_analyze(url):
    data = fetch_and_parse(url)
    df = analyze_data(data)
    save_to_csv(df, 'products.csv')
    return df

# Llamada a la función
url = 'http://example.com/products'
fetch_and_analyze(url)
