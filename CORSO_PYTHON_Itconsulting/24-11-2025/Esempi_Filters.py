""" def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers) )
print(even_numbers) # Output: [2, 4, 6, 8, 10]
 """

#ESERCIZIO:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #creo una lista di numeri
def condizione(i):  #per implementare la condizione di confronto
    if i == len(lista) - 1:
        return False
    if i >= len(lista) - 2:
        return lista[i] > lista[-1] and lista[i+1] > lista[-1]
    return lista[i] > lista[i+2] and lista[i+1] > lista[i+2]  #x confronta con x+2
risultato = list(filter(lambda i: condizione(i), range(len(lista))))  #uso filter (su iterabile) per confrontare elementi vicini

print("Indici che ammettono la condizione:", risultato)
print("Gruppi (x, x+1, x+2) validi", [lista[i] for i in risultato])


#ESERCIZIO VERSIONE MIRKO:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# funzione di filtro: prende un indice x
def somma_due_maggiore_del_terzo(x):
    return numbers[x] + numbers[x + 1] > numbers[x + 2]
# così x+1 e x+2 esisttono sempre
indici = range(len(numbers) - 2)
indici_validi = list(filter(somma_due_maggiore_del_terzo, indici))
gruppi_validi = [
    (numbers[i], numbers[i + 1], numbers[i + 2])
    for i in indici_validi
]
print("Indici che rispettano la condizione:", indici_validi)
print("Gruppi (x, x+1, x+2) validi:", gruppi_validi)