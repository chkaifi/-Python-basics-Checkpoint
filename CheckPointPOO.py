class Compte:
    def __init__(self, numero_de_compte: str, solde_du_compte: float, titulaire_du_compte: str):
        self.numero_de_compte = numero_de_compte
        self.solde_du_compte = solde_du_compte
        self.titulaire_du_compte = titulaire_du_compte

    def deposit(self, amount: float):
        """Ajoute le montant au solde du compte."""
        if amount > 0:
            self.solde_du_compte += amount
            print(f"Dépôt de {amount} effectué. Nouveau solde : {self.solde_du_compte}")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount: float):
        """Soustrait le montant si le solde est suffisant."""
        if amount <= self.solde_du_compte:
            self.solde_du_compte -= amount
            print(f"Retrait de {amount} effectué. Nouveau solde : {self.solde_du_compte}")
        else:
            print(f"Fonds insuffisants pour un retrait de {amount}. Solde actuel : {self.solde_du_compte}")

    def check_balance(self):
        """Renvoie le solde actuel."""
        return self.solde_du_compte

# --- Tests et Instances ---

# 1. Création de l'instance 'my_account'
my_account = Compte("FR76-001", 1000.0, "Alice")

# 2. Utilisation des méthodes
my_account.deposit(500.0)
my_account.withdraw(200.0)
print(f"Solde final de my_account : {my_account.check_balance()}")

print("-" * 30)

# 3. Test avec d'autres instances
compte_pro = Compte("FR76-002", 50.0, "Bob")
compte_pro.withdraw(100.0)  # Doit échouer (fonds insuffisants)
compte_pro.deposit(200.0)
print(f"Solde de Bob : {compte_pro.check_balance()}")
