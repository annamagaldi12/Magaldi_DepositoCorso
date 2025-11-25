#import libreria numpy
import numpy as np
from Parte_UNO import salva_su_file, m, sotto_matrice_centrale, trasponi, somma 

#moltiplicazione elemento per elemento
def moltiplicazione_elementwise(m): 
    r, c = m.shape
    print("Crea la seconda matrice con le STESSE dimensioni della prima.")
    m2 = np.random.randint(0, 100, size=(r, c))
    print("Seconda matrice:", m2)
    risultato = m * m2
    print("Moltiplicazione elemento per elemento:", risultato)
    salva_su_file(f"Moltiplicazione element-wise:{risultato}")


#Media elementi della matrice
def media(m):
    media = np.mean(m)
print("Media degli elementi:", media)
salva_su_file(f"Media degli elementi: {media}")


#Menù
def menu():
    matrice = None
    while True:
        print("\n--- MENU ---")
        print("1. Crea nuova matrice 2D")
        print("2. Estrai sotto-matrice centrale")
        print("3. Trasponi matrice")
        print("4. Somma elementi")
        print("5. Moltiplicazione elementoXelemento")
        print("6. Media elementi")
        print("7. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            matrice = matrice()
        elif scelta == "2":
            if matrice is not None:
                sotto_matrice_centrale(matrice)
            else:
                print("Crea una matrice!")
        elif scelta == "3":
            if matrice is not None:
                trasponi(matrice)
            else:
                print("Crea una matrice!")
        elif scelta == "4":
            if matrice is not None:
                somma(matrice)
            else:
                print("Crea prima una matrice!")
        elif scelta == "5":
            if matrice is not None:
                moltiplicazione_elementwise(matrice)
            else:
                print("Crea prima una matrice!")
        elif scelta == "6":
            if matrice is not None:
                media(matrice)
            else:
                print("Crea prima una matrice!")
        elif scelta == "7":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")