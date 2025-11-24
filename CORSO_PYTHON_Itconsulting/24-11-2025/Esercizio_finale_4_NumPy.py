#import la libreria numpy
import numpy as np 

# 1.
#Creazione dell’array arange e 50 valori casuali + 50 posizioni casuali
arr1 = np.arange(50)
arr2 = np.random.randint(49, 102, size=50)
arr = np.array([*arr1, *arr2])

#1.2 
#Stampa array, tipo e forma
print("Array partenza:\n", arr)
print("Dtype:", arr.dtype)
print("Shape:", arr.shape, "\n")

#2. 
#Conversione in float64
arr = arr.astype(np.float64)

#2.2 
#Stampa nuovo tipo-forma
print("Dopo conversione float64:")
print("Dtype:", arr.dtype)
print("Shape:", arr.shape, "\n")

#3.
#SLICING:
primi_10 = arr[:10] #slicing primi 10 elementi
ultimi_7 = arr[-7:] #slicing ultimi 7 elementi
da_5_a_20 = arr[5:20] #slicing da indice 5 a 20
ogni_quarto = arr[::4] #slicing ogni quarto elemento

#4. 
#Modifica elementi da indice 10 a 15 (escluso)
arr[10:15] = 999

#5. 
#FANCY INDEXING:
posizioni_specifiche = arr[[0, 3, 7, 12, 25, 33, 48]] #selezione posizioni specifiche:Fancy indexing
elementi_pari = arr[arr % 2 == 0] #elementi pari:Fancy indexing
elementi_maggiori_media = arr[arr > arr.mean()] #elementi maggiori della media:Fancy indexing

#6. 
#Stampa array modiificata e risultati slicing/fancy indexing:
print("Array modificata:\n", arr, "\n")

print("Primi 10 elementi:\n", primi_10, "\n")
print("Ultimi 7 elementi:\n", ultimi_7, "\n")
print("Elementi da 5 a 20:\n", da_5_a_20, "\n")
print("Ogni quarto elemento:\n", ogni_quarto, "\n")

print("Posizioni [0,3,7,12,25,33,48]:\n", posizioni_specifiche, "\n")
print("Elementi pari dell’array:\n", elementi_pari, "\n")
print("Elementi maggiori della media:\n", elementi_maggiori_media, "\n")
