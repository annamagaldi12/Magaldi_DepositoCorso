""" ##PRINT
#print("hello")

#print ('nome:', "Anna")
#print ('cognome:', "Magaldi")
#print ('età:', 25)

##INPUT
#nome = input ("scrivi il tuo nome")
#print("nome")

#nome = input("scrivi il tuo nome: ")
#eta = input("scrivi la tua età: ")
#print("Ciao, " + nome + "! Benventuo in Python!")")

#eta = input("scrivi la tua età: nome")


##tipo int
##sono i numeri positivi o negativi
#x = 10
#y = -10
#print(x,y)

##TIPO FLOAT
#sono i numeri con la virgola
#a = 10.5
#b = -7.3
#print(a,b)

##STRINGHE
#s = 'Ciao, Mondo!'
#print(len(s)) #Output: 12
#print(s.upper()) #Output: 'CIAO, MONDO!'
#print(s.split(',')) #Output: 'Ciao', ' Mondo!'
#print(s.replace('Mondo', 'Python')) #Output: 'Ciao, Universo!'

##CARATTERI
#char = 'A'
#print(char)

##BOOLEANI
#operatori logici: and, or, not
#x = 5
#y = 10
#z = 7
#print(x < y and y > z)  #Output: True
#print(x > y or y > z)   #Output: True
#print(not(x < y))       #Output: False

#BOOLEANI
#controlli di uguaglianza e maggioranza / minoranza  """

""" x = 5
y = 10
print(x == y)  #Output: False
print(x != y)  #Output: True
print(x < y)   #Output: True
print(x > y)   #Output: False
print(x <= y)  #Output: True
print(x >= y)  #Output: False """


""" #if - else
numero = 10
if numero > 0:
    print("Il numero è positivo.")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("Il numero è negativo")
else:
    print("Il numero è zero.") """
    
    
# Esercizio 1: tre livelli di controllo
""" print("Controllo 3 livelli")

livello1 = input("Inserisci la parola chiave del primo livello: ")

if livello1 == "abc":
    livello2 = input("Parola chiave di secondo livello: ")
    if livello2 == "123":
        livello3 = input("Parola chiave di terzo livello: ")
        if livello3 == "xyz":
            print("Accesso COMPLETO!")
        else:
            print("Terzo livello errato")
    else:
        print("Secondo livello errato")
else:
    print("Primo livello errato") """
    
# Esercizio 2:
print("1 - Aggiungi password")
print("2 - Rimuovi password")
print("3 - Visualizza password")
print("4 - Uscita")

scelta = input("Scegliere un'opzione (1-4): ")

if scelta == "1":
    print("Scelta: Aggiungi password")
elif scelta == "2":
    print("Scelta: Rimuovi password")
elif scelta == "3":
    print("Scelta: Visualizza password")
elif scelta == "4":
    print("Uscita")
else:
    print("Opzione nulla")
    
    