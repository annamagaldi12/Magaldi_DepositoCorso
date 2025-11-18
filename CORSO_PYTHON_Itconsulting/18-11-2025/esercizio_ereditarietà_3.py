#CLASSE BASE
class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
#Inizializza l'attributo 'nome' con il valore passato.
        self.nome = nome
#Inizializza l'attributo 'numero_soldati' con il valore passato.
        self.numero_soldati = numero_soldati

#Metodo per simulare il movimento dell'unità.
    def muovi(self):
        print(f"[{self.nome}]: Inizia a muoversi. {self.numero_soldati} soldati in marcia.")

#Metodo per simulare l'attacco dell'unità
    def attacca(self):
        print(f"[{self.nome}]: Ingaggia il nemico! Fuoco!")

#Metodo per gestire il ritiro strategico
    def ritira(self):
        print(f"[{self.nome}]: Esegue un ritiro strategico.")
        
#CLASSI DERIVATE:
class Fanteria(UnitaMilitare):
#Metodo specifico per la Fanteria: costruire difese
    def costruisci_trincea(self):
        print(f"[{self.nome}]: Costruisce trincee e fortificazioni difensive.")

#Classe Artiglieria: aggiunge la calibrazione dei pezzi
class Artiglieria(UnitaMilitare):
#Metodo specifico per l'Artiglieria: calibrare l'attrezzatura
    def calibra_artiglieria(self):
        print(f"[{self.nome}]: Calibra i pezzi di artiglieria per una maggiore precisione di tiro.")

#Classe Cavalleria: aggiunge l'esplorazione del terreno
class Cavalleria(UnitaMilitare):
    # Metodo specifico per la Cavalleria: esplorare l'area
    def esplora_terreno(self):
        # Stampa un messaggio sull'azione specifica.
        print(f"[{self.nome}]: Esplora il terreno circostante per raccogliere informazioni sul nemico.")

# 2.4 Classe SupportoLogistico: aggiunge il rifornimento delle unità
class SupportoLogistico(UnitaMilitare):
    # Metodo specifico per il Supporto Logistico: rifornire altre unità
    def rifornisci_unita(self):
        # Stampa un messaggio sull'azione specifica
        print(f"[{self.nome}]: Fornisce rifornimenti, carburante e manutenzione alle unità sul campo.")

# 2.5 Classe Ricognizione: aggiunge la conduzione di missioni di sorveglianza
class Ricognizione(UnitaMilitare):
    # Metodo specifico per la Ricognizione: sorveglianza
    def conduci_ricognizione(self):
        # Stampa un messaggio sull'azione specifica
        print(f"[{self.nome}]: Conduce missioni di sorveglianza e raccolta dati ad alto rischio.")
        
#CONTROLLO MILITARE:
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    #Il costruttore richiede gli stessi attributi di UnitaMilitare.
    def __init__(self, nome, numero_soldati):
        #Chiama il costruttore della prima classe base nell'ordine di ereditarietà (Fanteria),
        #che a sua volta chiama UnitaMilitare
        super().__init__(nome, numero_soldati)
        #La chiave sarà il nome dell'unità e il valore sarà l'oggetto unità.
        self.unita_registrate = {} 
        
    #Metodo per aggiungere un oggetto unità al registro.
    def registra_unita(self, unita):
        #Controlla che l'oggetto sia una classe unità (anche se ControlloMilitare è un'unità).
        if isinstance(unita, UnitaMilitare):
            #Usa il nome dell'unità come chiave per registrarla nel dizionario.
            self.unita_registrate[unita.nome] = unita
            print(f"*** Unità '{unita.nome}' di tipo {type(unita).__name__} registrata. ***")
        else:
            print("Errore: L'oggetto non è un'unità militare valida.")

    #Metodo per elencare tutte le unità registrate.
    def mostra_unita(self):
        print("\n--- Unità Militari Registrate ---")
        #Controlla se il registro è vuoto.
        if not self.unita_registrate:
            print("Nessuna unità è stata ancora registrata.")
            return
            
        #Itera sul dizionario delle unità.
        for nome, unita in self.unita_registrate.items():
            #Stampa il nome e il tipo (classe) dell'unità.
            print(f"- **{nome}** ({type(unita).__name__}): {unita.numero_soldati} soldati.")

    #Metodo per mostrare i dettagli di una specifica unità.
    def dettagli_unita(self, nome):
        #Verifica se l'unità è presente nel registro.
        if nome in self.unita_registrate:
            unita = self.unita_registrate[nome]
            print(f"\n--- Dettagli per Unità: {nome} ---")
            #Stampa gli attributi di base.
            print(f"Tipo: {type(unita).__name__}")
            print(f"Soldati: {unita.numero_soldati}")
            #Esempio di come chiamare un metodo base.
            unita.muovi() 
            #Esempio di come chiamare un metodo specifico, se noto.
            if isinstance(unita, Fanteria):
                unita.costruisci_trincea()
            elif isinstance(unita, Ricognizione):
                unita.conduci_ricognizione()
        else:
            print(f"Errore: Unità '{nome}' non trovata nel registro.")
    