from CLASSE_BASE import Elettrodomestico
from SOTTOCLASSI import Lavatrice, Frigorifero, Forno

#4.CLASSE OFFICINA:
class Officina:
    def __init__(self, nome):
        self.nome = nome
        self.tickets = []
    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)
    def chiudi_ticket(self, id_ticket):
        for t in self.tickets:
            if t.get_id_ticket() == id_ticket:
                t.set_stato("chiuso")
                return
        print("Ticket non trovato!")
    def stampa_ticket_aperti(self):
        for t in self.tickets:
            if t.get_stato() != "chiuso":
                elettro = t.get_elettrodomestico()
                print(f"ID: {t.get_id_ticket()}, Tipo: {type(elettro).__name__}, Stato: {t.get_stato()}")
    def totale_preventivi(self):
        totale = 0
        for t in self.tickets:
            totale += t.calcola_preventivo()
        return totale
    
    # statistiche per tipo- Type()
    def statistiche_per_tipo(self):
        contatori = {"Lavatrice": 0, "Frigorifero": 0, "Forno": 0}
        for t in self.tickets:
            elettro = t.get_elettrodomestico()
            if type(elettro) == Lavatrice:
                contatori["Lavatrice"] += 1
            elif type(elettro) == Frigorifero:
                contatori["Frigorifero"] += 1
            elif type(elettro) == Forno:
                contatori["Forno"] += 1
        for k, v in contatori.items():
            print(f"Numero di {k.lower()} in riparazione: {v}")