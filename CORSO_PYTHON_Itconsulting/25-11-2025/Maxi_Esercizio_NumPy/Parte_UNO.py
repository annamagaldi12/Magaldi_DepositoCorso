#import libreria numpy
import numpy as np

#salva su file
def salva_su_file(testo):
    with open("Parte_UNO.txt", "a") as f:
        f.write(testo + "\n")

#nuova matrice 2D casuale
def matrice_casuale():  #numeri casuali da 0 a 99
    righe = int(input("Inserire numero di righe: "))
    colonne = int(input("Inserire numero di colonne: "))
    matrice = np.random.randint(0, 100, size=(righe, colonne))
    print("Matrice:\n", matrice)
    salva_su_file(f"Matrice:\n{matrice}")
    return matrice

#Estrazione sotto-matrice centrale
def sotto_matrice_centrale(m):
    r, c = m.shape  # num.r= righe(prende da m.shape), num.c=colonnem(prende da m.shape) , m=matrice(param.funzione)
    r_centro = r // 2  #calcolo matrice centrale dividendo x 2
    c_centro = c // 2  #calcolo matrice centrale dividendo x 2

    if r % 2 == 1 and c % 2 == 1: #se r e c sono dispari = matrice ha centro singolo
        sub = m[r_centro-1:r_centro+2, c_centro-1:c_centro+2]
    else:
        sub = m[max(0, r_centro-1):r_centro+1, max(0, c_centro-1):c_centro+1]

    print("Sotto-matrice centrale:\n", sub)
    salva_su_file(f"Sotto-matrice centrale:\n{sub}")

#stampa+trasposizione matrice
def trasponi(m): #scambio di righe e colonne
    t = m.T
    print("Matrice trasposta:\n", t)
    salva_su_file(f"Matrice trasposta:\n{t}")

#Stampa+somma elementi matrice
def somma(m):
    s = np.sum(m)
    print("Somma degli elementi:", s)
    salva_su_file(f"Somma degli elementi: {s}")
