# ESERCIZIO 1: Incapsulamento in una classe ContoBancario

class ContoBancario:
    # Costruttore della classe ContoBancario
    def __init__(self, titolare, saldo_iniziale=0):
        self.__titolare = None
        self.__saldo = 0
        self.set_titolare(titolare)
        if saldo_iniziale >= 0:
            self.__saldo = saldo_iniziale
        else:
            raise ValueError("Il saldo iniziale non può essere negativo.")

    # Metodi per gestire il saldo
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito effettuato: {importo}. Saldo attuale: {self.__saldo}")
        else:
            print("Errore: l'importo da depositare deve essere positivo.")

    def preleva(self, importo):
        if importo <= 0:
            print("Errore: l'importo da prelevare deve essere positivo.")
        elif importo > self.__saldo:
            print("Errore: fondi insufficienti.")
        else:
            self.__saldo -= importo
            print(f"Prelievo effettuato: {importo}. Saldo attuale: {self.__saldo}")

    def visualizza_saldo(self):
        return self.__saldo

    # Getter e Setter per il titolare
    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, nome):
        nome_pulito = str(nome).strip()
        if nome_pulito:
            self.__titolare = nome_pulito
        else:
            raise ValueError("Il nome del titolare deve essere una stringa non vuota.")


# Funzione menu interattivo
def menu():
    print("\n=== MENU CONTO BANCARIO ===")
    print("1. Visualizza saldo")
    print("2. Deposita")
    print("3. Preleva")
    print("4. Modifica titolare")
    print("5. Mostra titolare")
    print("0. Esci")
    scelta = input("Seleziona un'opzione: ")
    return scelta


# Programma principale
# Creiamo un conto iniziale
nome_iniziale = input("Inserisci il nome del titolare del conto: ")
saldo_iniziale = float(input("Inserisci il saldo iniziale: "))
conto = ContoBancario(nome_iniziale, saldo_iniziale)

while True:
    scelta = menu()

    if scelta == "1":
        print(f"Saldo corrente: {conto.visualizza_saldo()}")
    elif scelta == "2":
        importo = float(input("Inserisci l'importo da depositare: "))
        conto.deposita(importo)
    elif scelta == "3":
        importo = float(input("Inserisci l'importo da prelevare: "))
        conto.preleva(importo)
    elif scelta == "4":
        nuovo_titolare = input("Inserisci il nuovo nome del titolare: ")
        try:
            conto.set_titolare(nuovo_titolare)
            print(f"Titolare aggiornato a: {conto.get_titolare()}")
        except ValueError as e:
            print(e)
    elif scelta == "5":
        print(f"Titolare corrente: {conto.get_titolare()}")
    elif scelta == "0":
        print("Uscita dal programma.")
        break
    else:
        print("Opzione non valida. Riprova.")
