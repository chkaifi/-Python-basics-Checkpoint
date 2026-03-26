import tkinter as tk

def fahrenheit_to_celsius():
    """Convertit la valeur de Fahrenheit en Celsius et met à jour l'étiquette de résultat."""
    fahrenheit = ent_temperature.get()
    try:
        # Conversion de la chaîne saisie en nombre flottant
        temp_f = float(fahrenheit)
        # Formule de conversion : (F - 32) * 5/9
        temp_c = (temp_f - 32) * 5 / 9
        # Mise à jour de l'affichage avec l'arrondi à 2 décimales
        lbl_result["text"] = f"{round(temp_c, 2)} \N{DEGREE CELSIUS}"
    except ValueError:
        # Gestion d'erreur si l'utilisateur saisit autre chose qu'un nombre
        lbl_result["text"] = "Erreur"

# Création de la fenêtre principale
window = tk.Tk()
window.title("Convertisseur de température")
window.resizable(width=False, height=False)

# Création du cadre (Frame) pour l'entrée
frm_entry = tk.Frame(master=window)

# Création du champ de saisie (Entry)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Disposition des widgets dans le cadre avec grid
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Création du bouton de conversion
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius  # Appelle la fonction lors du clic
)

# Création de l'étiquette pour le résultat
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Disposition des éléments principaux dans la fenêtre
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Lancement de l'application
window.mainloop()
