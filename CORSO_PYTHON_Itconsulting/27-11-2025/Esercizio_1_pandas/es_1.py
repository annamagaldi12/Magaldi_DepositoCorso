import pandas as pd
import numpy as np

# 1.Caricamento dataset Titanic da URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# 2.Inseriamo valori mancanti casuali solo in alcune colonne
np.random.seed(42)
n = len(df)

df['Age'] = df['Age'].where(np.random.rand(n) >= 0.1, np.nan)
df['Embarked'] = df['Embarked'].where(np.random.rand(n) >= 0.05, np.nan)
df['Cabin'] = df['Cabin'].where(np.random.rand(n) >= 0.3, np.nan)

print("Valori mancanti iniziali:")
print(df[['Age','Embarked','Cabin']].isna().sum())

# 2a.prime e ultime 5 righe
print("\nPrime 5 righe:")
print(df.head())
print("\nUltime 5 righe:")
print(df.tail())


# 3.tipo di dati delle colonne
print("\nTipi di dati delle colonne:")
print(df.dtypes)

# 4.Statistiche descrittive (media, mediana, std)
print("\nStatistiche descrittive (numeriche):")
print(df[['Age','SibSp','Parch','Fare']].agg(['mean','median','std']))

# 5.Identificare e rimuovere duplicati
duplicati = df.duplicated().sum()
print(f"\nNumero di duplicati: {duplicati}")
df = df.drop_duplicates()

# 6.Gestione valori mancanti
df['Age'] = df['Age'].fillna(df['Age'].median())  #fillna = riempire valori mancanti
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['HasCabin'] = df['Cabin'].notna().astype(int)
df = df.drop(columns=['Cabin'])
print("\nValori mancanti dopo gestione:")
print(df[['Age','Embarked','HasCabin']].isna().sum())


# 7. Creazione colonna Categoria Età
def categoria_eta(a):
    if a <= 18:
        return 'Giovane'
    elif a <= 65:
        return 'Adulto'
    else:
        return 'Senior'
df['Categoria_Età'] = df['Age'].apply(categoria_eta)


# 8. Salvataggio del dataset pulito
df.to_csv('titanic_cleaned_completo.csv', index=False)


print("\nDataFrame pulito:")
print(df.head())
