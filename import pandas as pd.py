import pandas as pd

# Asume que 'products' es la lista de diccionarios extraídos en el paso anterior
df = pd.DataFrame(products)

# Limpiar datos
df['price'] = df['price'].str.replace('$', '').astype(float)
df['availability'] = df['availability'].apply(lambda x: True if x == 'In stock' else False)

# Análisis básico
average_price = df['price'].mean()
print(f'Average price: ${average_price:.2f}')

# Guardar datos en un archivo
df.to_csv('products.csv', index=False)
