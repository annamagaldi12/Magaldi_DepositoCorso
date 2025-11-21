
from GestoreFlotta import GestoreFlotta # type: ignore
from VeicoloTrasporto import Camion, Furgone, Motocarro # type: ignore


#MAIN
if __name__ == "__main__":
    # Creo il gestore della flotta
    flotta = GestoreFlotta()

    # Creo alcuni veicoli
    camion1 = Camion("AB123CD", 10000, 4)
    furgone1 = Furgone("FG456HI", 3000, "diesel")
    motocarro1 = Motocarro("LM789NO", 800, 10)

    # Aggiungo alla flotta
    flotta.aggiungi_veicolo(camion1)
    flotta.aggiungi_veicolo(furgone1)
    flotta.aggiungi_veicolo(motocarro1)

    print("\n--- Caricamento Merci ---")
    camion1.carica(2000)
    furgone1.carica(500)
    motocarro1.carica(300)

    print("\n--- Stato Veicoli ---")
    flotta.stampa_veicoli()

    print("\n--- Costo totale manutenzione ---")
    print(f"{flotta.costo_totale_manutenzione()} €")

    print("\n--- Rimozione veicolo ---")
    flotta.rimuovi_veicolo("FG456HI")

    print("\n--- Flotta aggiornata ---")
    flotta.stampa_veicoli()