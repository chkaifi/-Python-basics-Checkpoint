import math

class Calculatrice:
    def __init__(self):
        # Initialisation du dictionnaire avec les fonctions de base
        # On utilise des fonctions lambda pour les opérations simples
        self.operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else float('nan') # Gestion division par zéro
        }

    def add_operation(self, symbole, fonction):
        """Ajoute une nouvelle opération au dictionnaire."""
        self.operations[symbole] = fonction
        print(f"Opération '{symbole}' ajoutée avec succès.")

    def calculer(self, a, symbole, b):
        """Exécute le calcul en vérifiant la validité des entrées."""
        
        # Vérification de la nature numérique (isinstance)
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            message = "Erreur : Les valeurs d'entrée doivent être des nombres."
            print(message)
            raise ValueError(message)

        # Vérification de la validité du symbole
        if symbole not in self.operations:
            message = f"Erreur : L'opération '{symbole}' n'est pas supportée."
            print(message)
            raise KeyError(message)

        # Exécution de l'opération
        try:
            resultat = self.operations[symbole](a, b)
            
            # Gestion spécifique pour la division par zéro ou erreurs mathématiques
            if isinstance(resultat, float) and math.isnan(resultat):
                raise ZeroDivisionError("Division par zéro impossible.")
                
            return resultat
        except Exception as e:
            print(f"Erreur lors du calcul : {e}")
            raise

# --- Fonctions pour les opérations avancées ---

def exponentiation(a, b):
    return math.pow(a, b)

def racine_carree(a, b=None):
    # 'b' est ignoré ici car la racine carrée est unitaire, 
    # mais la méthode calculer envoie 3 arguments.
    if a < 0:
        raise ValueError("La racine carrée d'un nombre négatif est impossible.")
    return math.sqrt(a)

def logarithme(a, b):
    # Logarithme de 'a' en base 'b'
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Paramètres de logarithme invalides.")
    return math.log(a, b)

# --- Programme Principal ---

def main():
    calc = Calculatrice()

    # Ajout des opérations avancées
    calc.add_operation('^', exponentiation)
    calc.add_operation('sqrt', racine_carree)
    calc.add_operation('log', logarithme)

    print("\n--- Bienvenue dans la Calculatrice Python ---")
    print("Opérations disponibles : +, -, *, /, ^, sqrt, log")

    while True:
        choix = input("\nAppuyez sur 'Entrée' pour calculer ou tapez 'quitter' pour sortir : ").lower()
        if choix == 'quitter':
            break

        try:
            # Récupération des entrées
            num1 = float(input("Entrez le premier nombre : "))
            op = input("Entrez le symbole de l'opération : ")
            
            # Pour 'sqrt', le deuxième nombre ne sert à rien mais est requis par la méthode
            num2 = 0
            if op != 'sqrt':
                num2 = float(input("Entrez le second nombre : "))

            # Calcul et affichage
            resultat = calc.calculer(num1, op, num2)
            print(f"Résultat : {resultat}")

        except ValueError:
            print("Erreur de saisie : Veuillez entrer des nombres valides.")
        except Exception as e:
            print(f"Calcul interrompu : {e}")

if __name__ == "__main__":
    main()
