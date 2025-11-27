import pandas as pd
import numpy as np

#1.
#Generare range di dati per periodo di un mese:
date_range = pd.date_range(start='2025-01-01', end='2025-01-30')
# città e prodotti
città = ['Roma', 'Torino', 'Napoli']
prodotti = ['Laptop', 'Cellulare', 'Auto Aziendale']
#dataframe vuoto da riempire
data = []
#ciclo per generare vendite casuali per ogni dato/città/prodotto
for date in date_range:
    for city in città:
        for products in prodotti:
            sales = np.random.randint(10, 100)  #vendite casuali
            data.append([date, city, products, sales])
#creare dataframe
df = pd.DataFrame(data, columns=['Data', 'Città', 'Prodotto', 'Vendite'])

""" #per verificare il tipo di dato
print("Tipi di dato nel DataFrame:\n", df.dtypes)
print("\nPrime righe del DataFrame:\n", df.head()) """

#2.Tabella pivot
pivot = df.pivot_table(
    values='Vendite', 
    index='Città', 
    columns='Prodotto', 
    aggfunc='mean'
)

print("\nPivot Table - Vendite medie per città-prodotto:\n", pivot)

#3.groupby
vendite_tot = df.groupby('Prodotto')['Vendite'].sum()  #raggruppa dataframe x prodotto + somma vendite totali 
print(vendite_tot)

