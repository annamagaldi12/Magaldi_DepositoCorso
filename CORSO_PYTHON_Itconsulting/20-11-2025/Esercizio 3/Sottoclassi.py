
from ClasseBase import Elettrodomestico
#2. SOTTOCLASSI:
#Lavatrice
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)  # eredita attributi base
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga
    # override del metodo stima_costo_base
    def stima_costo_base(self):
        costo = 60
        if self.__capacita_kg > 7: #maggiore capacità, costo maggiore
            costo += 20
        return costo
#Frigorifero
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer
    def stima_costo_base(self):
        costo = 70
        if self.__litri > 300:
            costo += 15
        if self.__ha_freezer:
            costo += 20
        return costo
#Forno
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato
    def stima_costo_base(self):
        costo = 55
        if self.__tipo_alimentazione == "gas":
            costo += 15
        if self.__ha_ventilato:
            costo += 10
        return costo

