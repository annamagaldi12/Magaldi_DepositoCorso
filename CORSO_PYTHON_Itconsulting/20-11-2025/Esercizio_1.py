#ESERCIZIO 1:

#CLASSE BASE MetodoPagamento:
class MetodoPagamento:
    #Metodo comune sovrascritto dalle sottoclassi
    def effettua_pagamento(self, importo):
        print("Metodo di pagamento non specificato.")

#SOTTOCLASSE - carta di credito
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito.")

#SOTTOCLASSE - PayPal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato tramite PayPal.")

#SOTTOCLASSE - bonifico bancario
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato tramite Bonifico Bancario.")


#CLASSE che si occupa del pagamento senza preoccuparsi del metodo di pagamento
class GestorePagamenti:

    def __init__(self, metodo):
        self.metodo = metodo

    def paga(self, importo): #
        self.metodo.effettua_pagamento(importo)



#EXTRA --- MENU' INTERATTIVO:
print("=== MENU METODO DI PAGAMENTO ===")
print("1. Carta di Credito")
print("2. PayPal")
print("3. Bonifico Bancario")

scelta = input("Scegli un metodo (1-2-3): ")

#Inizializzazione del metodo preferito
if scelta == "1":
    metodo = CartaDiCredito()
elif scelta == "2":
    metodo = PayPal()
elif scelta == "3":
    metodo = BonificoBancario()
else:
    print("Scelta non valida. Uso il metodo di default.")
    metodo = MetodoPagamento()

# Chiediamo l'importo da pagare
importo = float(input("Inserisci l'importo da pagare: "))

# Creiamo un GestorePagamenti con il metodo scelto
gestore = GestorePagamenti(metodo)

# Eseguimo il pagamento
gestore.paga(importo)