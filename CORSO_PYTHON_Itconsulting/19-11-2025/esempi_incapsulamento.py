#INCAPSULAMENTO
class Computer:
 def __init__(self):
   self.__processore = "Intel i5" # Attributo privato
 def get_processore(self):
   return self.__processore
 def set_processore(self, processore):
   self.__processore = processore
pc = Computer()
print(pc.get_processore()) 

# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5") 

# Modifica l'attributo privato tramite il setter
print(pc.get_processore())


#CONTENIMENTO/INCAPSULAMENTO
class Computer:
 def __init__(self, nome_proc):
   self.__processore = nome_proc # Attributo privato
 def get_processore(self):
   return self.__processore
 def set_processore(self, processore):
   self.__processore = processore
pc = Computer("Intel i5")
print(pc.get_processore()) 
# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5") 
# Modifica l'attributo privato tramite il setter
print(pc.get_processore())



#PRIVATI:
class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
    def __metodo_privato(self):
        return "Questo è un metodo privato"
obj = MiaClasse()
# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata)  # AttributeError
# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata)  # Funzionerà, ma non è buona prassi



#PROTETTI
class ClasseBase:
    def __init__(self):
        self._variabile_protetta = "Sono protetta"
class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta)  # Accesso consentito
obj = SottoClasse()
# Accesso da fuori la classe (non consigliato, ma possibile)
print(obj._variabile_protetta)


