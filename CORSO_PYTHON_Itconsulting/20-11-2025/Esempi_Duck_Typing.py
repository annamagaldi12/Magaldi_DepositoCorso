
 # Esempio di Duck Typing
class Cane:
    def parla(self):
        return "Bau!"
    
class Gatto:
    def parla(self):
        return "Miao!"
def fai_parlare(animale):
    # Non importa di che tipo sia l'animale,
    print(animale.parla())
cane = Cane()
gatto = Gatto()
fai_parlare(cane)  # Output: Bau!
fai_parlare(gatto)  # Output: Miao!


#ESEMPIO 2:
class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")
        
class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")
def disegna_figura(figura):
    # Anche qui, basta che 'figura' abbia il metodo 'disegna'
    figura.disegna()
figure = [Cerchio(), Rettangolo()]     # figure[0]=Cerchio() / figure[1]=Rettagolo()
# Iteriamo e disegniamo ogni figura
for figura in figure:
    disegna_figura(figura)