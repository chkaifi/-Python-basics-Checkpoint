# Question 1 :Multiplier les éléments d'une liste

liste = [2, 3, 6]
resultat = 1

for x in liste:
    resultat *= x

print(resultat) # Affiche 36







#Question 2 : Trier des tuples par leur dernier élément

liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# On définit une fonction qui renvoie le dernier élément
def dernier_element(n):
    return n[-1]

liste.sort(key=dernier_element)
print(liste) # Affiche [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]







#Question 3 : Combiner deux dictionnaires (addition)

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

resultat = Counter(d1) + Counter(d2)
print(dict(resultat)) # Affiche {'a': 400, 'b': 400, 'c': 300, 'd': 400}






#Question 4 : Dictionnaire de carrés (1 à n)

n = 8
dictionnaire = {}

for i in range(1, n + 1):
    dictionnaire[i] = i * i

print(dictionnaire)






#Question 5 : Trier des tuples par valeur flottante (ordre décroissant)

liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# On trie en convertissant le texte en nombre (float)
liste.sort(key=lambda x: float(x[1]), reverse=True)
print(liste)








#Question 6 : Manipuler les ensembles (Set)

# 1. Créer un ensemble
mon_ensemble = {0, 1, 2, 3, 4}

# 2. Itérer (boucler) sur l'ensemble
for element in mon_ensemble:
    print(f"Élément : {element}")

# 3. Ajouter et Supprimer
mon_ensemble.add(5)      # Ajoute 5
mon_ensemble.discard(2)  # Supprime 2 (ne fait rien s'il n'existe pas)

print(mon_ensemble) 
