#import libreria numpy
import numpy as np
# 1. 
#matrice 5x5 con numeri sequenziali da 1 a 25
matrice = np.arange(1, 26).reshape(5, 5) 
# 2. 
#Estrarre e stampare la seconda colonna
seconda_col = matrice[:, 1]
# 3.
#terza riga
terza_riga = matrice[2, :]
# 4. 
#somma della diagonale principale
diagonale_sum = np.trace(matrice)
# 5. 
#Stampa
print("\nMatrice 5x5:\n", matrice)
print("Seconda colonna:", seconda_col)
print("Terza riga:", terza_riga)
print("Somma della diagonale principale:", diagonale_sum)
