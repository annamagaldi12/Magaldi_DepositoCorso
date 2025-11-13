#ESERCIZIO 1: 
# Scrivi un programma che chieda all'utente se vuole inserire un numero o una stringa.
# Se l'utente sceglie di inserire un numero, il programma deve determinare se il numero è pari o dispari e stampare il risultato.
# Se l'utente sceglie di inserire una stringa, il programma deve stampare ogni carattere della stringa su una nuova riga.  
while True:
    scelta = input("Vuoi inserire un 'numero' o una 'stringa'? ").strip().lower()

    if scelta == "numero":
        valore = int(input("Inserisci un numero: "))
        if valore % 2 == 0:
            print(f"{valore} è un numero PARI.")
        else:
            print(f"{valore} è un numero DISPARI.")

    elif scelta == "stringa":
        testo = input("Inserisci una stringa: ")
        lunghezza = len(testo)
        print(f"La stringa contiene {lunghezza} caratteri.")

        if lunghezza % 2 == 0:
            print("Il numero di caratteri è PARI.")
        else:
            print("Il numero di caratteri è DISPARI.")

    else:
        print("Scelta non valida. Scrivi 'numero' o 'stringa'.")
        continue

    # Chiede se ripetere
    ripeti = input("Vuoi ripetere? (s/n): ").strip().lower()
    if ripeti != "s":
        print("Programma terminato.")
        break
    
    
    
#ESERCIZIO 2:
def è_primo(n):
    if n < 2:  #i numeri minori di 2 non sono primi
        return False
    for i in range(2, int(n**0.5) + 1):  #controlla i divisori fino alla radice quadrata di n
        if n % i == 0:
            return False
    return True

while True:  #ciclo principale
    inizio = int(input("Inserisci il numero di inizio intervallo: "))
    fine = int(input("Inserisci il numero di fine intervallo: "))

    numeri_primi = []  #liste vuote
    numeri_non_primi = []  #liste vuote

    for num in range(inizio, fine + 1):
        if è_primo(num):
            numeri_primi.append(num)
        else:
            numeri_non_primi.append(num)

    scelta = input("Vuoi vedere 'primi', 'non primi' o 'entrambi'? ").strip().lower()

    if scelta == "primi":
        print("Numeri primi:", numeri_primi)
    elif scelta == "non primi":
        print("Numeri non primi:", numeri_non_primi)
    elif scelta == "entrambi":
        print("Numeri primi:", numeri_primi)
        print("Numeri non primi:", numeri_non_primi)
    else:
        print("Scelta non valida.")

    ripeti = input("Vuoi ripetere? (s/n): ").strip().lower()
    if ripeti != "s":
        print("Programma terminato.")
        break
