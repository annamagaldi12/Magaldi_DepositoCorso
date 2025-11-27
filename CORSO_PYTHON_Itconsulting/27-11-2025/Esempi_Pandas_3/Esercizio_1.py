import pandas as pd
import numpy as np
#-----------------------------------------------------#
#-----------------------------------------------------#

np.random.seed(42) #numeri casuali
n_clienti = 60 #numero clienti

#ID Cliente
ID_Cliente = np.arange(1, n_clienti + 1)  #array da 1 a 60 che sono ID clienti)
#Età casuale
Età = np.random.randint(18, 61, n_clienti) #età casuali tra 18 e 60
#Durata abbonamento: più breve => più probabilità di churn
Durata_Abbonamento = np.random.randint(1, 13, n_clienti) #da 1 a 12 mesi e chi ha una durata minore ha piu prob. di "appendere" (quindi: Churn)
#Tariffa mensile: più alta => meno churn
Tariffa_Mensile = np.round(np.random.uniform(2, 10, n_clienti), 2)  #da 2 a 10
#Dati consumati: maggiore => meno churn
Dati_Consumati = np.random.randint(50, 201, n_clienti)
#Contatti servizio clienti: più contatti => più churn
Servizio_Clienti_Contatti = np.random.randint(1, 11, n_clienti) #da 1 a 11
#Probabilità di churn 
prob_churn = 0.3 + (6 - Durata_Abbonamento) * 0.03 + (Servizio_Clienti_Contatti - 1) * 0.04  #Aggiungo 0.03(30%prob) x ogni mese sotto i 6 mesi. Aggiungo 0.04 x ogni contatto sopra 1
prob_churn = np.clip(prob_churn, 0, 1) #limito i valori tra 0 e 1
#Generazione Churn casuale
Churn = np.array(['Sì' if np.random.rand() < p else 'No' for p in prob_churn]) #x ogni cliente genera un num.cas. tra 0 e 1. Se num.cas< della probob. di churn allora "Si"(appende), altrimenti no
#Creazione DataFrame
dati_clienti = pd.DataFrame({  #inserimento colonne in tabella pandas
    'ID_Cliente': ID_Cliente,
    'Età': Età,
    'Durata_Abbonamento': Durata_Abbonamento,
    'Tariffa_Mensile': Tariffa_Mensile,
    'Dati_Consumati': Dati_Consumati,
    'Servizio_Clienti_Contatti': Servizio_Clienti_Contatti,
    'Churn': Churn
})

#ordino dati
dati_clienti.sort_values(by=['Churn', 'ID_Cliente'], ascending=[True, True], inplace=True)


# Salvataggio CSV
dati_clienti.to_csv("clienti_TIM_completo.csv", index=False)
print("File CSV realistico generato: clienti_TIM_completo.csv")

#-----------------------------------------------------#
#-----------------------------------------------------#

#analisi dati
#1. caricamento file
dati = pd.read_csv("clienti_TIM.csv")

print(dati.info()) #vediamo info

# Statistiche descrittive
print(dati.describe()) #mostta statistiche
# Distribuzione della colonna churn
print(dati['Churn'].value_counts()) #value_counts conta quanti clienti hanno appeso

# 2. Pulizia dei dati
# Sostituzione dei valori mancanti con la mediana
for col in ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']:
    dati[col].fillna(dati[col].median(), inplace=True)
# Correzione anomalie (ho settato l'età da 18 a 60 e tariffa tra 0 e 10)
dati = dati[(dati['Età'] >= 18) & (dati['Età'] <= 60)]
dati = dati[(dati['Tariffa_Mensile'] >= 0) & (dati['Tariffa_Mensile'] <= 10)]

# 3. Analisi esplorativa
#nuova colonna: costo per GB usato
dati['Costo_per_GB'] = dati['Tariffa_Mensile'] / dati['Dati_Consumati']
#relazione tra variabili e Churn
print(dati.groupby('Età')['Churn'].value_counts(normalize=True))
print(dati.groupby('Durata_Abbonamento')['Churn'].value_counts(normalize=True))
print(dati.groupby('Tariffa_Mensile')['Churn'].value_counts(normalize=True))

print(dati.corr())

# 4.modellazione
# Conversione colonna Churn --> numerico
dati['Churn_Num'] = dati['Churn'].map({'No': 0, 'Sì': 1}) 
# Selezione colonne numeriche
colonne_numeriche = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile',
                     'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']

X = dati[colonne_numeriche].values #matrice (variabili num)
y = dati['Churn_Num'].values #target (churn)
# Normalizzazione Min-Max
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_normalizzato = (X - X_min) / (X_max - X_min)


    

