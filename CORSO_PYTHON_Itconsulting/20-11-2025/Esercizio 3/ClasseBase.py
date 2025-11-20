#ESERCIZIO 3: GESTIONALE DI UN'OFFICINA DI ELETTRODOMESTICI
#1.CLASSE BASE Elettrodomestico:   
class Elettrodomestico:
    def __init__(self, marca, modello, anno_acquisto, guasto):
        self.__marca = marca                 # privato, incapsulato
        self._modello = modello               # protetto
        self.__anno_acquisto = anno_acquisto  # privator
        self._guasto = guasto                 # protetto
    
    # getter - marca
    def get_marca(self):
        return self.__marca

    # setter - marca
    def set_marca(self, marca):
        self.__marca = marca

    # getter - modello
    def get_modello(self):
        return self._modello

    # setter - modello
    def set_modello(self, modello):
        self._modello = modello

    # getter - anno_acquisto
    def get_anno_acquisto(self):
        return self.__anno_acquisto

    # setter con controllo
    def set_anno_acquisto(self, anno):
        import datetime
        if anno <= datetime.datetime.now().year:
            self.__anno_acquisto = anno
        else:
            print("Anno di acquisto non valido!")

    # getter - guasto
    def get_guasto(self):
        return self._guasto

    # setter - guasto
    def set_guasto(self, guasto):
        self._guasto = guasto

    # descrizione dell'elettrodomestico
    def descrizione(self):
        return f"Marca: {self.__marca}, Modello: {self._modello}, " \
               f"Anno: {self.__anno_acquisto}, Guasto: {self._guasto}"

    # stima costo base generico
    def stima_costo_base(self):
        return 50  # costo base generico - diagnosi
