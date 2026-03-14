import pandas as pd

# 1. Création du DataFrame
data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'], 
    'Age': [30, 40, 25, 35, 45, 28], 
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'], 
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000], 
    'Experience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)

# 2. Utilisation de iloc pour sélectionner les 3 premières lignes (index 0 à 2)
first_three_rows = employee_df.iloc[:3]

# 3. Utilisation de loc pour sélectionner le département "Marketing"
marketing_dept = employee_df.loc[employee_df['Department'] == 'Marketing']

# 4. Utilisation de iloc pour sélectionner Age et Gender (colonnes index 2 et 3) pour les 4 premières lignes
age_gender_subset = employee_df.iloc[:4, [2, 3]]

# 5. Utilisation de loc pour sélectionner Salaire et Expérience pour les hommes ("Male")
male_compensation = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]

# --- Affichage des résultats ---

print("--- 3 premières lignes (iloc) ---")
print(first_three_rows)

print("\n--- Département Marketing (loc) ---")
print(marketing_dept)

print("\n--- Age et Genre des 4 premiers (iloc) ---")
print(age_gender_subset)

print("\n--- Salaire et Expérience des Hommes (loc) ---")
print(male_compensation)
