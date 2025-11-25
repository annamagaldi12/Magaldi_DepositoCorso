#import libreria numpy
import numpy as np
#1. 
#array 15 numeri casuali tra 1 e 100(inclusi)
array = np.random.randint(1, 101, 15) 
#2. 
#somma di tutti gli elementi di array
sum_array = np.sum(array)
#3. 
#Calcolare la media di tutti gli elementi
media_array = np.mean(array)  # np.mean calcola la media aritmetica
# 4. 
#Stampa
print("Array casuale 1D:", array)
print("Somma degli elementi:", sum_array)
print("Media degli elementi:", media_array)
