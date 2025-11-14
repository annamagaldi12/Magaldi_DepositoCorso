#ESERCIZIO 1:

#1.leggere un intero positivo usando while
numeri_inseriti = []  #lista per salvare i numeri inseriti

while True:  #ciclo while per assicurarsi che l'input sia valido
    n = int(input("Inserisci un numero intero positivo n: "))
    if n <= 0:
        print("Il numero deve essere positivo (> 0). Riprova.")
        continue
    numeri_inseriti.append(n)  #salvataggio numero inserito
    break  #usciamo dal ciclo nel caso in cui sia positivo

#2.somma dei numeri pari da 1 a n usando FOR con RANGE
somma_pari = 0
for i in range(2, n + 1, 2):
    somma_pari += i
print("\nSomma dei numeri pari da 1 a", n, ":", somma_pari)

#3.stampare tutti i numeri dispari da 1 a n
numeri_dispari = []
print("\nNumeri dispari da 1 a", n, ":")
for i in range(1, n + 1, 2):
    numeri_dispari.append(i)
    print(i)

#4.controllare se n è un numero primo
def è_primo(n):
    if n < 2:   #i numeri < 2 non sono primi
        return False
    for i in range(2, n):  #controlla tutti i numeri da 2 a n-1
        if n % i == 0:
            return False
    return True

if è_primo(n):
    print(f"\n{n} è un numero PRIMO.")
else:
    print(f"\n{n} non è un numero PRIMO.")
    
#5.lista in cui salviamo gli input degli utenti
print("\nLista dei numeri inseriti dall'utente:", numeri_inseriti)