#Esercizio 1
somma = 0 #variabile per tenere traccia della somma

while True:
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    if numero == 0:
        break   # Termina il ciclo se l'utente inserisce 0
    somma += numero  # Aggiunge il numero alla somma totale

print("La somma totale dei numeri inseriti è:", somma)



#Esercizio 2
parola = input("Inserisci una parola: ")  #Chiede all'utente di inserire una parola

for lettera in parola:  #Itera attraverso ogni lettera della parola
    print(lettera)  #Stampa ogni lettera su una nuova riga
    
    
    
#Esercizio 3
N = int(input("Inserisci il numero massimo (N): "))  #Chiede all'utente di inserire il numero massimo
step = int(input("Inserisci lo step: "))  #Chiede all'utente di inserire lo step

for i in range(0, N + 1, step):   #Itera da 0 a N con lo step specificato
    print(i)