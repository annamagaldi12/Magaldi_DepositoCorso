#Creo la classe base MembroSquadra
class MembroSquadra:
    def __init__(self, nome, eta): #Il metodo __init__ serve per inizializzare gli attributi della classe
        self.nome = nome       #Salvo il nome del membro della squadra
        self.eta = eta         #Salvo l'età del membro della squadra

    #Metodo che stampa una descrizione generale del membro della squadra
    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni, è un membro della squadra.")
        

#Creo la classe Giocatore che eredita da MembroSquadra
class Giocatore(MembroSquadra):
    #Il giocatore ha attributi extra: ruolo e numero della maglia
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)   # Richiamo il costruttore della classe madre
        self.ruolo = ruolo            # Attributo aggiuntivo: ruolo del giocatore
        self.numero_maglia = numero_maglia  # Attributo extra: numero sulla maglia

    #Metodo specifico del giocatore
    def gioca_partita(self):
        print(f"{self.nome} (#{self.numero_maglia}) entra in campo come {self.ruolo}!")

#Creo la classe Allenatore che eredita da MembroSquadra
class Allenatore(MembroSquadra):
    #L'allenatore ha un attributo extra: anni di esperienza
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)   # Richiamo il costruttore della classe madre
        self.anni_di_esperienza = anni_di_esperienza  # Attributo aggiuntivo

    #Metodo specifico dell'allenatore
    def dirige_allenamento(self):
        print(f"{self.nome} dirige l'allenamento con {self.anni_di_esperienza} anni di esperienza.")


#Creo la classe Assistente che eredita da MembroSquadra
class Assistente(MembroSquadra):
    # L'assistente ha un attributo extra: specializzazione
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)   # Richiamo il costruttore della classe madre
        self.specializzazione = specializzazione  # Attributo aggiuntivo

    #Metodo specifico dell'assistente
    def supporta_team(self):
        print(f"{self.nome}, specializzato in {self.specializzazione}, supporta la squadra.")


#ESEMPIO D'USO
g1 = Giocatore("Luca", 24, "attaccante", 9)
g1.descrivi()          #Metodo ereditato
g1.gioca_partita()     #Metodo della classe Giocatore

#Creo un allenatore
a1 = Allenatore("Mister Rossi", 52, 20)
a1.descrivi()          #Metodo ereditato
a1.dirige_allenamento()  #Metodo della classe Allenatore

#Creo un assistente
as1 = Assistente("Marco", 35, "fisioterapista")
as1.descrivi()          #Metodo ereditato
as1.supporta_team()     #Metodo della classe Assistente
