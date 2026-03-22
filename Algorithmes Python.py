# 1️⃣ Recherche binaire
def recherche_binaire(liste, cible):
    gauche = 0
    droite = len(liste) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2
        
        if liste[milieu] == cible:
            return True
        elif liste[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return False


# 2️⃣ Puissance (a^b)
def puissance(a, b):
    resultat = 1
    for _ in range(b):
        resultat *= a
    return resultat


# 3️⃣ Tri à bulles
def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


# 4️⃣ Tri fusion
def tri_fusion(liste):
    if len(liste) <= 1:
        return liste

    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])

    return fusion(gauche, droite)


def fusion(gauche, droite):
    resultat = []
    i = j = 0

    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat


# 5️⃣ Tri rapide
def tri_rapide(liste):
    if len(liste) <= 1:
        return liste

    pivot = liste[0]
    inferieur = [x for x in liste[1:] if x <= pivot]
    superieur = [x for x in liste[1:] if x > pivot]

    return tri_rapide(inferieur) + [pivot] + tri_rapide(superieur)


# =========================
# TESTS
# =========================

print("Recherche binaire :")
print(recherche_binaire([1,2,3,5,8], 6))  # False
print(recherche_binaire([1,2,3,5,8], 5))  # True

print("\nPuissance :")
print(puissance(3,4))  # 81

liste_test = [29,13,22,37,52,49,46,71,56]

print("\nTri à bulles :")
print(tri_bulles(liste_test.copy()))

print("\nTri fusion :")
print(tri_fusion(liste_test.copy()))

print("\nTri rapide :")
print(tri_rapide(liste_test.copy()))
