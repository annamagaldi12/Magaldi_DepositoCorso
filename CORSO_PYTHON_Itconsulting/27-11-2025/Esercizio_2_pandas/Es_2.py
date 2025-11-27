import pandas as pd

#1.
#dataset delle vendite
data = {
    "Prodotto": ["latte", "pane", "salume", "frutta", "verdura"],
    "Quantità": [5, 10, 20, 50, 25],
    "Prezzo Unitario": [20, 50, 15, 20, 50],
    "Città": ["Roma (Coop)", "Milano (365)", "Torino (Lidl)", "Roma (EuroSpin)", "Napoli (Dodecà)"]
}

#Creo un DataFrame a partire dal dizionario
df = pd.DataFrame(data)

#2.
#Aggiungiamo la colonna "Totale Vendite" = Quantità * Prezzo Unitario
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]

#3.
#Raggruppo per prodotto e sommo le vendite
totale_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum()

#4.
#prodotto più venduto (in base alla Quantità)
prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].sum().idxmax()

#5.
#città con il maggior totale di vendite
citta_top = df.groupby("Città")["Totale Vendite"].sum().idxmax()

#6.
#filtro solo le vendite superiori a 1000 euro
vendite_alte = df[df["Totale Vendite"] > 1000]

#7.
#ordinoi il DataFrame originale per Totale Vendite (dal più grande al più piccolo)
df_ordinato = df.sort_values(by="Totale Vendite", ascending=False)

#8.
#conto quante vendite ci sono in ogni città
numero_vendite_per_citta = df["Città"].value_counts()



#stampa
print("DataFrame originale con Totale Vendite:\n", df, "\n")
print("Totale vendite per prodotto:\n", totale_per_prodotto, "\n")
print("Prodotto più venduto:", prodotto_piu_venduto, "\n")
print("Città con maggior volume di vendite totali:", citta_top, "\n")
print("Vendite superiori a 1000 euro:\n", vendite_alte, "\n")
print("DataFrame ordinato per Totale Vendite decrescente:\n", df_ordinato, "\n")
print("Numero di vendite per città:\n", numero_vendite_per_citta)
