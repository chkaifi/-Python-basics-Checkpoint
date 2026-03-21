import numpy as np

# 1. Ouverture du fichier (en utilisant le contexte 'with' pour la sécurité)
file_path = 'Loan_prediction_dataset.csv'

# Nous utilisons genfromtxt pour extraire la colonne 'LoanAmount'
# La colonne 'LoanAmount' est la 9ème colonne (index 8)
try:
    data = np.genfromtxt(
        file_path, 
        delimiter=',', 
        skip_header=1, 
        usecols=8, 
        filling_values=0
    )

    # 2. Analyses statistiques
    mean_loan = np.mean(data)
    median_loan = np.median(data)
    std_loan = np.std(data)

    print(f"--- Analyse des Montants des Prêts ---")
    print(f"Moyenne : {mean_loan:.2f}")
    print(f"Médiane : {median_loan:.2f}")
    print(f"Écart-type : {std_loan:.2f}")

except Exception as e:
    print(f"Erreur lors de la lecture du fichier : {e}")
