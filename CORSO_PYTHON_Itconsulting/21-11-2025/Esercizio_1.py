from abc import ABC, abstractmethod

#CLASSE ASTRATTA
class VeicoloTrasporto(ABC): # La classe eredita da ABC → diventa astratta
    def __init__(self, targa, peso_massimo):
        # Attributi protetti
        self._targa = targa #attributo protetto
        self._peso_massimo = peso_massimo #attributo protetto
        self._carico_attuale = 0

    def carica(self, peso):
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"Caricati {peso} kg. Carico attuale: {self._carico_attuale} kg.")
        else:
            print("Error: il peso supera la capacità massima di carico.")

    def scarica(self):
        self._carico_attuale = 0
        print("Carico scaricato completamente.")

    @abstractmethod
    def costo_manutenzione(self):
        pass


#SOTTOCLASSI CONCRETE
class Camion(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo, numero_assi):
        super().__init__(targa, peso_massimo) #eredito il costruttore della superclasse
        self.numero_assi = numero_assi #attributo specifico
    def costo_manutenzione(self):
        return (100 * self.numero_assi) + (1 * self._peso_massimo)

class Furgone(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo, alimentazione):
        super().__init__(targa, peso_massimo)
        self.alimentazione = alimentazione

    def costo_manutenzione(self): 
        if self.alimentazione == "elettrico":
            return 200
        else:
            return 150

class Motocarro(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo)
        self.anni_servizio = anni_servizio

    def costo_manutenzione(self):
        return 50 * self.anni_servizio


#GESTORE FLOTTA
class GestoreFlotta:
    def __init__(self):
        self.veicoli = []
    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)
        print(f"Veicolo {veicolo._targa} aggiunto alla flotta.")
    def rimuovi_veicolo(self, targa):
        for v in self.veicoli:
            if v._targa == targa:
                self.veicoli.remove(v)
                print(f"Veicolo {targa} rimosso.")
                return
        print("Targa non trovata.")
    def costo_totale_manutenzione(self):
        totale = 0
        for v in self.veicoli:
            totale += v.costo_manutenzione()  # polimorfismo
        return totale
    def stampa_veicoli(self):
        for v in self.veicoli:
            print(f"Targa: {v._targa}, Tipo: {type(v).__name__}, Carico: {v._carico_attuale} kg")


