# Guardar datos en archivo CSV
df.to_csv('products.csv', index=False)

# Leer datos de archivo CSV
df = pd.read_csv('products.csv')
print(df.head())
