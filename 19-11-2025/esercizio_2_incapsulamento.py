#ESERCIZIO 2: INCAPSULAMENTO, POLIMORFISMO, EREDITARIETA'

#1:
# Classe base - Persona (incapsulamento)
class Persona: #persona è la classe base
    def __init__(self, nome, eta):
        # Attributi privati
        self.__nome = nome
        self.__eta = eta
    # Getter - nome
    def get_nome(self):
        return self.__nome
    # Setter - nome
    def set_nome(self, nome):
        self.__nome = nome
    # Getter - età
    def get_eta(self): #
        return self.__eta 
    # Setter - età
    def set_eta(self, eta):
        self.__eta = eta
    # Metodo presentazione generico
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.__nome} e ho {self.__eta} anni.")

#2:
# Sottoclasse Studente che eredita da Persona (ereditarietà e polimorfismo)
class Studente(Persona): #studente eredita da Persona
    def __init__(self, nome, eta, voti):
        # Inizializzo nome ed età usando il costruttore della superclasse
        super().__init__(nome, eta)
        # Attributo specifico dello studente
        self.__voti = voti
    # Getter e setter - voti
    def get_voti(self):
        return self.__voti
    def set_voti(self, voti):
        self.__voti = voti
    # calcolo media dei voti
    def calcola_media(self):
        if len(self.__voti) == 0:
            return 0
        return sum(self.__voti) / len(self.__voti)
    # Override metodo presentazione (polimorfismo)
    def presentazione(self):
        media = self.calcola_media()
        print(f"Ciao, mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e la mia media è {media:.2f}.")

#3:
# Sottoclasse Professore che eredita da Persona (polimorfismo)
class Professore(Persona):  #professore eredita da Persona
    def __init__(self, nome, eta, materia):
        # Inizializzo nome ed età usando il costruttore della superclasse
        super().__init__(nome, eta)
        # Attributo specifico del professore
        self.__materia = materia
    # Getter e setter - materia
    def get_materia(self):
        return self.__materia
    def set_materia(self, materia):
        self.__materia = materia
    # Override metodo presentazione (polimorfismo)
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.get_nome()}, ho {self.get_eta()} anni e insegno {self.__materia}.")


#4:
# Creazione oggetto Studente
studente1 = Studente("Anna", 30, [8, 7, 9])
studente1.presentazione()  # Output: presentazione con media dei voti
# Creazione oggetto Professore
professore1 = Professore("Mirko", 32, "Python")
professore1.presentazione()  # Output: presentazione con materia insegnata

#CREAZIONE MENU' INTERATTIVO
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Studente")
        print("2. Professore")
        print("3. Esci")
        scelta = input("Scegli un'opzione (1-3): ")

        if scelta == "1":
            studente1.presentazione()
        elif scelta == "2":
            professore1.presentazione()
        elif scelta == "3":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova.")

# Avvio menù
menu()