import sqlite3
import os
import csv
import math
from Esempi_Sql_2 import clean_data


#4. salva dataset su sqlite
db_data_filename = "california_clean.db"
if os.path.exists(db_data_filename):
    os.remove(db_data_filename)
print(f"\n--- Creo DB dati: {db_data_filename} ---")

conn_data = sqlite3.connect(db_data_filename)
cursor_data = conn_data.cursor()
cursor_data.execute("""
CREATE TABLE IF NOT EXISTS housing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    longitude REAL,
    latitude REAL,
    housing_median_age REAL,
    total_rooms REAL,
    total_bedrooms REAL,
    population REAL,
    households REAL,
    median_income REAL,
    median_house_value REAL
);
""")

# Inserimento dati puliti
sql_insert = """
INSERT INTO housing (
    longitude, latitude, housing_median_age,
    total_rooms, total_bedrooms, population,
    households, median_income, median_house_value
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
for row in clean_data:
    cursor_data.execute(sql_insert, (
        row["longitude"], row["latitude"], row["housing_median_age"],
        row["total_rooms"], row["total_bedrooms"], row["population"],
        row["households"], row["median_income"], row["median_house_value"]
    ))
conn_data.commit()
conn_data.close()
print("✔ Dataset pulito salvato in california_clean.db")