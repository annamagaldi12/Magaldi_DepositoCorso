import csv

# Dati da scrivere
rows = [
    ["Data", "Prodotto", "Quantità", "Prezzo_unitario", "Totale"],
    ["2025-01-01", "Laptop", 2, 1200, 2400],
    ["2025-01-02", "Mouse", 5, 25, 125],
    ["2025-01-03", "Monitor", 1, 300, 300],
]

# Nome del file CSV
file_name = "vendite.csv"

# Scrittura del CSV
with open(file_name, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("CSV creato correttamente!")