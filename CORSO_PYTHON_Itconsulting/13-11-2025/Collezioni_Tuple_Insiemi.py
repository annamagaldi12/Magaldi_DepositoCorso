# Esempi di tuple in Python
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 30, "Femmina")


#insiemi in Python
set1 = ([1, 2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}

set3 = {1, 2, 3, 3, 4, 4, 5}  # I duplicati verranno rimossi automaticamente
print(set3)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))         # Unione: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))  # Intersezione: {4, 5}
print(set1.difference(set2))    # Differenza: {1, 2, 3}
print(set1.symmetric_difference(set2))  # Differenza simmetrica: {1, 2, 3, 6, 7, 8}

