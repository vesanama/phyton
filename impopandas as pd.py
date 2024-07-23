import pandas as pd

def analyze_data(data):
    df = pd.DataFrame(data)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    df['availability'] = df['availability'].apply(lambda x: True if x == 'In stock' else False)
    return df.describe()

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
