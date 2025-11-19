# ESERCIZIO 3: GESTIONE DI UN PARCO VEICOLI CON INCAPSULAMENTO E EREDITARIETÀ


# CLASSE BASE: VEICOLO
class Veicolo:
    def __init__(self, marca, modello, anno):
        # Attributi Privati
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False  #stato accensione spento

    def accendi(self):
        # Cambia lo stato di accensione a True
        self._accensione = True
        print(f"{self._marca} {self._modello} è ora acceso.")

    def spegni(self):
        # Cambia lo stato di accensione a False
        self._accensione = False
        print(f"{self._marca} {self._modello} è ora spento.")



# CLASSE DERIVATA: AUTO
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        # Richiama il costruttore della classe base
        super().__init__(marca, modello, anno)
        self._numero_porte = numero_porte

    def suona_clacson(self):
        # Metodo specifico dell’auto
        print("Beep!")


# CLASSE DERIVATA: FURGONE
class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacità_carico):
        super().__init__(marca, modello, anno)
        self._capacità_carico = capacità_carico  # in kg
    def carica(self):
        print(f"Il furgone {self._marca} sta caricando merce.")
    def scarica(self):
        print(f"Il furgone {self._marca} sta scaricando la merce.")


# CLASSE DERIVATA: MOTOCICLETTA
class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self._tipo = tipo  # sportiva, touring, custom...
    def esegui_wheelie(self):
        # Esegue la wheelie solo se sportiva
        if self._tipo.lower() == "sportiva":
            print("Sto facendo una wheelie!!!")
        else:
            print("Questa moto non è sportiva, no wheelie.")


# CLASSE: GESTORE PARCO VEICOLI
class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []  # lista vuota all'inizio
    def aggiungi_veicolo(self, veicolo):
        # Aggiunge un veicolo alla lista
        self._veicoli.append(veicolo)
        print(f"Veicolo {veicolo._marca} {veicolo._modello} aggiunto al parco.")
    def rimuovi_veicolo(self, marca, modello):
        # Cerca un veicolo con marca e modello specificato
        for v in self._veicoli:
            if v._marca == marca and v._modello == modello:
                self._veicoli.remove(v)
                print(f"Veicolo {marca} {modello} rimosso dal parco.")
                return
        print("Veicolo non trovato.")
    def lista_veicoli(self):
        # Stampa tutti i veicoli nel parco
        if not self._veicoli:
            print("Il parco veicoli è vuoto.")
        else:
            print("\n--- VEICOLI NEL PARCO ---")
            for v in self._veicoli:
                print(f"{v._marca} {v._modello} - Anno: {v._anno}")


# UTILIZZO DELLE CLASSI
auto1 = Auto("Yunday", "I-20", 2021, 5)
furgone1 = Furgone("Ford", "Transit", 2020, 1200)
moto1 = Motocicletta("Yamaha", "R1", 2022, "Sportiva")

gestore = GestoreParcoVeicoli()

gestore.aggiungi_veicolo(auto1)
gestore.aggiungi_veicolo(furgone1)
gestore.aggiungi_veicolo(moto1)

gestore.lista_veicoli()

auto1.suona_clacson()
moto1.esegui_wheelie()


#MENU INTERATTIVO
