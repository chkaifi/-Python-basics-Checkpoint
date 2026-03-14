import numpy as np

# 1. Création du tableau des notes
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# 2. Calcul des mesures statistiques
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# 3. Valeurs maximales et minimales
max_grade = np.max(grades)
min_grade = np.min(grades)

# 4. Tri des notes par ordre croissant
sorted_grades = np.sort(grades)

# 5. Indice de la note la plus élevée
index_max = np.argmax(grades)

# 6. Analyse des performances (Seuil > 90)
count_above_90 = np.sum(grades > 90)
percentage_above_90 = np.mean(grades > 90) * 100

# 7. Analyse des échecs (Seuil < 75)
# Note : Dans cet échantillon, aucune note n'est strictement inférieure à 75
percentage_below_75 = np.mean(grades < 75) * 100

# 8. Extraction de sous-ensembles (Masquage booléen)
high_performers = grades[grades > 90]
passing_grades = grades[grades > 75]

# --- Affichage des résultats ---

print("--- Analyse Statistique des Notes ---")
print(f"Notes originales : {grades}")
print(f"Notes triées : {sorted_grades}")
print(f"Moyenne : {mean_grade:.2f}")
print(f"Médiane : {median_grade}")
print(f"Écart-type : {std_deviation:.2f}")
print(f"Note Max : {max_grade} (à l'indice {index_max})")
print(f"Note Min : {min_grade}")

print("\n--- Segments d'étudiants ---")
print(f"Nombre d'étudiants > 90 : {count_above_90}")
print(f"Pourcentage d'étudiants > 90 : {percentage_above_90}%")
print(f"Pourcentage d'étudiants < 75 : {percentage_below_75}%")

print("\n--- Sous-tableaux ---")
print(f"High Performers (>90) : {high_performers}")
print(f"Passing Grades (>75) : {passing_grades}")
