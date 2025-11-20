#ESERCIZIO 2:

#CLASSE BASE: rappresenta un posto generico in teatro
class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Ok! Posto {self._fila}{self._numero} prenotato correttamente.")
        else:
            print(f"Attenzione: Posto {self._fila}{self._numero} già occupato!")
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} libero.")
        else:
            print(f"Posto {self._fila}{self._numero} non prenotato.")
    def get_numero(self):
        return self._numero
    def get_fila(self):
        return self._fila
    def is_occupato(self):
        return self._occupato
    #POLIMORFISMO: per sapere il tipo del posto
    def tipo(self):
        return "Standard"


#CLASSE VIP:
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto VIP {self._fila}{self._numero} prenotato!")
            print("Servizi extra attivati:", ", ".join(self.servizi_extra))
        else:
            print(f"Attenzione: Posto VIP {self._fila}{self._numero} già occupato!")

    def tipo(self):
        return "VIP"

#CLASSE STAMDARD:
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila)
        self.costo = costo
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto Standard {self._fila}{self._numero} prenotato!")
            print(f"Costo della prenotazione: {self.costo}€")
        else:
            print(f"Attenzione: Posto Standard {self._fila}{self._numero} già occupato!")

    def tipo(self):
        return "Standard"


#CLASSE TEATRO:
class Teatro:
    def __init__(self):
        self._posti = []
    def aggiungi_posto(self, posto):
        self._posti.append(posto)
    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()  #Polimorfismo
                return
        print("Posto non trovato!")
    def stampa_posti_occupati(self):
        print("\n--- Posti Occupati ---")
        for posto in self._posti:
            if posto.is_occupato():
                print(f"{posto.tipo()}: {posto.get_fila()}{posto.get_numero()}")
        print("----------------------")


#MAIN:
def main():
    teatro = Teatro()
    # Aggiungo posti Standard
    teatro.aggiungi_posto(PostoStandard(1, "A", 15))
    teatro.aggiungi_posto(PostoStandard(2, "A", 15))
    teatro.aggiungi_posto(PostoStandard(3, "A", 15))
    # Aggiungo posti VIP
    teatro.aggiungi_posto(PostoVIP(1, "B", ["Accesso Lounge", "drink inclusi"]))
    teatro.aggiungi_posto(PostoVIP(2, "B", ["Accesso Lounge", "servizio posto"]))
    # Prenotazioni di prova
    teatro.prenota_posto(1, "A")
    teatro.prenota_posto(2, "B")
    teatro.prenota_posto(1, "B")
    teatro.prenota_posto(1, "A")
    # Stampiamo i posti occupati
    teatro.stampa_posti_occupati()

if __name__ == "__main__":
    main()
