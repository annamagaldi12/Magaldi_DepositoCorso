#import libreria numpy
import numpy as np

# Crea 12 numeri equidistanti tra 0 e 1
array = np.linspace(0, 1, 12)

# Cambia l'array 1D in una matrice 3x4
matr = array.reshape(3, 4)

#matrice casuale 3x4
rand_mat = np.random.random((3, 4))

#somma di ciascuna matrice
sum_matr = np.sum(matr)
sum_rand = np.sum(rand_mat)

#Stampa
print("mat1 (da linspace):\n", matr)
print("Somma mat1:", sum_matr)
print("\nrand_mat (numeri casuali 3x4):\n", rand_mat)
print("Somma rand_mat:", sum_rand)
