""" #LISTE
numeri = [1, 2, 3, 4, 5]
print(len(numeri))
numeri.append
print
numeri.insert(2, 10)
print(numeri)
numeri.remove(4)
print(numeri)
 """
 
 #Esercizio 1:

 #credenziali:
 Username_corretto = "admin"
 Password_corretta = "12345"
 
 #input utente
 username = input("Inserisci il username: ")
 Password = input("Inserisci la password: ")
 
 #verifica credenziali
 if username == Username_corretto and Password == Password_corretta:
     print("Accesso effettuato! Benvenuto, admin.")
 else:
     print("Credenziali errate! Accesso negato.")
 