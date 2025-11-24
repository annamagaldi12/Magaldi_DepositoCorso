import numpy as np #import libreria numpy 

#1.
#creazione matrice 2D 6X6 di numeri interi casuali tra 1 e 100 (101 escluso)
matrice = np.random.randint(1, 101, size=(6, 6))

#2.
#slicing per prendere righe e colonne da 1 a 4 (4 escluso)
sottomatrice = matrice[1:5, 1:5] 

#3.
#[::-1] per invertire l'ordine delle righe della sottomatrice
sott_invertita = sottomatrice[::-1]

#4.
#estrazione diag principale che restituisce un array 1D
diag = np.diag(sott_invertita)

#5.
#modifica della sott_matrice: sostituisci multipli di 3 con -1 usando np.where
sott_modificata = np.where(sott_invertita % 3 == 0, -1, sott_invertita)

#6.
#stampa delle matrici prodotte
print("Matrice (6x6):\n", matrice, "\n")
print("Sottomatrice (4x4):\n", sottomatrice, "\n")
print("Sottomatrice invertita:\n", sott_invertita, "\n")
print("Diagonale - matrice invertita:\n", diag, "\n")
print("Sottomatrice modificata:\n", sott_modificata)
