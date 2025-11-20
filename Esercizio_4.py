#IMPORT del modulo ABC per creare classi astratte
from abc import ABC, abstractmethod

#CLASSE ASTRATTA: Impiegato
class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

#SOTTOCLASSE:
#Impiegato Fisso
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base

#Impiegato a Provvigione
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale_bonus):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale_bonus = percentuale_bonus

    def calcola_stipendio(self):
        bonus = self.vendite * self.percentuale_bonus
        return self.stipendio_base + bonus

#Stampa info impiegati
def stampa_info(impiegato):
    print(f"Nome: {impiegato.nome} {impiegato.cognome}")
    print(f"Stipendio mensile: {impiegato.calcola_stipendio()}€")
    print("----------------------")

# MAIN
if __name__ == "__main__":
    # Creo alcuni impiegati
    imp1 = ImpiegatoFisso("Anna", "Magaldi", 1500)
    imp2 = ImpiegatoAProvvigione("Mirko", "Campari", 2000, vendite=5000, percentuale_bonus=0.10)
    
    # Lista di impiegati
    impiegati = [imp1, imp2]
    
    # Stampo info per tutti gli impiegati
    for imp in impiegati:
        stampa_info(imp)
