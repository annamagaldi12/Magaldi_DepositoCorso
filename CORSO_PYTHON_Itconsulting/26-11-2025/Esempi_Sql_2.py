import sqlite3
import os
import csv
import math

#1. caricame4nto dataset da csv
csv_filename = "california_housing_data.csv"
print("\n--- Caricamento dataset da CSV ---")
with open(csv_filename, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(f"Righe lette: {len(data)}")

numerical_cols = [    #colonne dal CSV
    "longitude", "latitude", "housing_median_age",
    "total_rooms", "total_bedrooms", "population",
    "households", "median_income", "median_house_value"
]

#2. pulizia dataset
clean_data = []
for row in data:
    cleaned_row = {}
    skip_row = False
    for col in numerical_cols:
        val = row[col].strip()
        if val == "" or val.lower() == "nan":
            skip_row = True      #elimino righe con valori mancanti
            break
        try:
            cleaned_row[col] = float(val)
        except:
            skip_row = True
            break
    if not skip_row:
        clean_data.append(cleaned_row)
print(f"Righe dopo pulizia: {len(clean_data)}")



#5. 2°DATABASE  (non ancora corretto)
db_stat_filename = "california_stat.db"
if os.path.exists(db_stat_filename):
    os.remove(db_stat_filename)
print(f"\n--- Creo DB statistiche: {db_stat_filename} ---")

conn_stat = sqlite3.connect(db_stat_filename)
cursor_stat = conn_stat.cursor()
cursor_stat.execute("""
CREATE TABLE IF NOT EXISTS stats (
    variabile TEXT PRIMARY KEY,
    minimo REAL,
    massimo REAL,
    media REAL,
    mediana REAL,
    deviazione_standard REAL
);
""")
sql_insert_stats = """
INSERT INTO stats (variabile, minimo, massimo, media, mediana, deviazione_standard)
VALUES (?, ?, ?, ?, ?, ?)
"""
for col, s in stats.items():
    cursor_stat.execute(sql_insert_stats, (
        col, s["min"], s["max"], s["media"], s["mediana"], s["dev_std"]
    ))
conn_stat.commit()
conn_stat.close()
print("✔ Statistiche salvate in california_stats.db")
print("\n--- FINE SCRIPT ---")