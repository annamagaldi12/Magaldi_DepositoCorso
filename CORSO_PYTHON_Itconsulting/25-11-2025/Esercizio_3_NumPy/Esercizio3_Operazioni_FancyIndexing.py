#import libreria numpy
import numpy as np

# 1. 
#array 4x4 di numeri casuali interi tra 10 e 50
array = np.random.randint(10, 51, (4, 4))  # 4x4 array con interi tra 10 e 50 inclusi

# 2. 
#elementi specifici-fancy indexing
righe = [0, 1, 2, 3]  #indici delle righe
colonne = [1, 3, 2, 0]  #indici delle colonne
elementi_selezionati = array[righe, colonne]  #elementi agli indici specificati

# 3. 
#Selezionare tutte le righe dispari
righe_dispari = array[1::2, :] 

# 4. 
#Modificare gli elementi selezionati (in fancy indexing) aggiungendo 10
array[righe, colonne] += 10

# 5. 
#Stampare i risultati
print("\nArray 4x4 + modifica:\n", array)
print("Elementi selezionati pre-modifica:", elementi_selezionati)
print("Righe dispari:\n", righe_dispari)
