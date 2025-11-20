from Classe_officina import Officina
from Sottoclassi import Lavatrice, Frigorifero, Forno
from ClasseBase import Elettrodomestico

def main():
    # Creo elettrodomestici
    lav = Lavatrice("Ariston", "LX200", 2019, "non centrifuga", 8, 1200)
    fri = Frigorifero("Samsung", "Cool500", 2020, "non raffredda", 350, True)
    forno = Forno("Whirlpool", "OvenX", 2021, "resistenza rotta", "elettrico", True)

    # Creo ticket
    t1 = TicketRiparazione(1, lav)
    t2 = TicketRiparazione(2, fri)
    t3 = TicketRiparazione(3, forno)

    # Creo officina e aggiungo ticket
    officina = Officina("Officina Centrale")
    officina.aggiungi_ticket(t1)
    officina.aggiungi_ticket(t2)
    officina.aggiungi_ticket(t3)

    # Stampiamo ticket aperti
    officina.stampa_ticket_aperti()

    # Aggiungo note
    t1.aggiungi_nota("Attendere pezzi di ricambio")
    t2.aggiungi_nota("Controllare gas refrigerante")

    # Calcolo preventivi con voci extra
    print("Preventivo lavatrice:", t1.calcola_preventivo(15, 10))  # base + 15 +10
    print("Preventivo frigorifero:", t2.calcola_preventivo(20))
    print("Preventivo forno:", t3.calcola_preventivo())

    # Statistiche per tipo
    officina.statistiche_per_tipo()

    # Totale preventivi
    print("Totale preventivi:", officina.totale_preventivi())

if __name__ == "__main__":
    main()
