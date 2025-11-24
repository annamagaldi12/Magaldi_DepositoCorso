import numpy as np  #importo la libreria numpy

arr = np.arange(10, 50) 
#arr= array multidimensionale
#creazione di np.arange= array di numeri da 10 a 49 (start=10, stop=50(non incluso))

print("Tipo di dato (dtype):", arr.dtype)  #dtype= tipo di dato dell'array

arr_float = np.arange(10, 50, dtype=np.float64) #Creazione array con tipo di dato float64 (ovvero num.decimali)
print("Nuovo tipo di dato (dtype):", arr_float.dtype)

print("Forma array (shape):", arr_float.shape) #.shape= elemnti presenti in ogni dimensione di array
#stampa forma dell'array

