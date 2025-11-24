import numpy as np #import libreria numpy

#1.
#ccreazione array di 20 numeri interi casuali tra 10 e 50
arr = np.random.randint(10, 51, size=20) 
#arr= ndarray monodimensionale con 20 elementi
#np.random.randint(start, stop, size) genera numeri interi casuali (start=10, stop=51, size=20)

print("Array di partenza:", arr) #stampa array di partenza

#2.
primi_10 = arr[:10]  #slicing: estraziojne dall'indice 0 al 9. Estrazione dei primi 10 elementi
print("\nPrimi 10 elementi:", primi_10)

#3.
ultimi_5 = arr[-5:]  #slicing: estrazione dagli ultimi 5 elementi fino alla fine
print("\nUltimi 5 elementi:", ultimi_5)

#4.
da_5_a_15 = arr[5:15] #slicing: estrazione dall'indice 5 al 14
print("\nElementi dal 5 al 15 (escluso):", da_5_a_15)

#5.
ogni_tre = arr[::3]  #slicing: estrazione dall'inizio alla fine con step ogni 3
print("\nOgni terzo elemento:", ogni_tre)

#6.
arr[5:10] = 99  #Modifica gli elementi dall'indice 5 al 9 impostandoli a 99

#7.
print("\nArray modificata:", arr)

