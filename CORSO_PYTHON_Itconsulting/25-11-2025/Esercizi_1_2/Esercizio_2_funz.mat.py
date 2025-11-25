#import libreria numpy
import numpy as np
import os #import libreria os per operazioni sul sistema operativo

#1.array 50 numeri equidistanti tra 10 e 50
array = np.linspace (10, 50, 5) 
#2.array 5 numeri casuali tra 0 e 1
random_array = np.random.rand(5) 
#3.Sommma tra i due array
sum_array = array + random_array
#4.Somma totalee degli elementi del terzo array
total_sum = np.sum(sum_array)
#5.Somma del terzo array > 5
sum_maggiore_5 = np.sum(sum_array[sum_array > 5])
#6. Stampa i risultati
print("Array (0-10):\n", array)
print("\nArray random (0-1):\n", random_array)
print("\nSomma array:\n", sum_array)
print("\nSomma totale elementi:", total_sum)
print("Somma > 5:", sum_maggiore_5)

#7. Salvataggop dati in file .txt
file_name = "Esercizio_2_funz.txt"

#8. Processo ripetibile ad ogni giro
with open(file_name, "w") as file:  #apertura file in modalita scrittura "w "
    file.write("Array (0-10):\n")
    np.savetxt(file, array)  #salvataggio array nel file
    file.write("\nArray random (0-1):\n")
    np.savetxt(file, random_array)
    file.write("\nSomma array:\n")
    np.savetxt(file, sum_array)
    file.write(f"\nSomma totale elementi: {total_sum:}\n")
    file.write(f"Somma > 5: {sum_maggiore_5:}\n")
    

#9. Richiesta sovrascrittura file in .txt
if os.path.exists(file_name):  #controlla se il file esiste
    risposta = input(f"Il file '{file_name}' esiste. Vuoi sovrascriverlo? (y/n): ").lower()
    if risposta != "y":  #se esiste il file, chiedo se sovrascriverlo o no
        print("File non sovrascritto.")
        exit()
        
        
print(f"\nDati salvati su '{file_name}'.")
