#FUNZIONI


#ESERCIZIO 1:
import random

def indovina_numero():
    numero_casuale = random.randint(1, 100)
    print("Ho scelto un numero tra 1 e 100. Quale è?")
    
    while True:
        tentativo = input("Inserisci un numero o digita 'esci' per uscire: ")
        
        if tentativo.lower() == "esci":
            print(f"Hai deciso di uscire. Il numero era {numero_casuale}.")
            break
        
        if not tentativo.isdigit():
            print("Inserisci un numero valido")
            continue
        
        tentativo = int(tentativo)
        
        if tentativo < numero_casuale:
            print("Troppo basso!")
        elif tentativo > numero_casuale:
            print("Troppo alto!")
        else:
            print("Hai indovinato il numero!")
            break

# Eseguire il gioco
indovina_numero()

#ESERCIZIO 2:
def fibonacci_fino_a(N):  #funzione fibonacci_fino_a(N) che genera la sequenza fino a N
    fib = [0, 1]  # iniziamo con i primi due numeri della sequenza
    
    while fib[-1] + fib[-2] <= N:
        fib.append(fib[-1] + fib[-2])
    
    return fib

# Chiedere numero N all'utente
N = int(input("Inserisci un numero N: "))
sequenza = fibonacci_fino_a(N)
print("Sequenza di Fibonacci fino a", N, ":")
print(sequenza)

