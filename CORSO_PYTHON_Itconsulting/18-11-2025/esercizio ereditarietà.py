#ESERCIZIO EREDITARIETA'

#CLASSE BASE: ANIMALE
class Animale:  #Creo la classe base che rappresenta un animale generico
    def __init__(self, nome, eta):
        #Inizializza gli attributi comuni a tutti gli animali
        self.nome = nome        # nome dell'animale
        self.eta = eta          # età dell'animale

    def fai_suono(self):
        #Metodo generico: le classi figlie potranno sovrascriverlo
        print("L'animale emette un suono generico.")

#CLASSE FIGLIA: LEONE
class Leone(Animale):  #eredita da Animale
    def fai_suono(self):
        #Sovrascrive il suono generico con un ruggito
        print("Il leone ruggisce: Roar!")

    def caccia(self):
        #Metodo specifico del leone
        print(f"{self.nome} sta cacciando nella savana")


#CLASSE FIGLIA: GIRAFFA
class Giraffa(Animale):  #eredita da Animale
    def fai_suono(self):
        #Sovrascrive il suono
        print("La giraffa emette un verso leggero.")
    def mangia_foglie(self):
        #Metodo specifico della giraffa
        print(f"{self.nome} sta mangiando foglie")


#CLASSE FIGLIA: PINGUINO
class Pinguino(Animale):  #eredita da Animale
    def fai_suono(self):
        #Sovrascrive il suono
        print("Il pinguino fa: 'Gwak Gwak!'")
    def nuota(self):
        #Metodo specifico del pinguino
        print(f"{self.nome} sta nuotando nell'acqua ghiacciata")


#ESEMPIO DI UTILIZZO
# Creiamo un leone
simba = Leone("Lion", 5)
simba.fai_suono()   # suono specifico del leone
simba.caccia()      # metodo speciale del leone

# Creiamo una giraffa
gira = Giraffa("Gira", 7)
gira.fai_suono()
gira.mangia_foglie()

# Creiamo un pinguino
pingu = Pinguino("Pingu", 3)
pingu.fai_suono()
pingu.nuota()
