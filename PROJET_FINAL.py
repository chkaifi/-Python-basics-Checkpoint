import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

class EcoTrack:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoTrack - Gestionnaire de Budget")
        self.root.geometry("500x550")
        self.filename = "depenses.csv"
        
     
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Description", "Catégorie", "Montant"])

        self.setup_ui()
        self.charger_donnees()

    def setup_ui(self):
        """Configure l'interface utilisateur."""
     
        frame_saisie = tk.LabelFrame(self.root, text=" Ajouter une dépense ", padx=10, pady=10)
        frame_saisie.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_saisie, text="Description:").grid(row=0, column=0, sticky="w")
        self.ent_desc = tk.Entry(frame_saisie)
        self.ent_desc.grid(row=0, column=1, pady=5, sticky="we")

        tk.Label(frame_saisie, text="Catégorie:").grid(row=1, column=0, sticky="w")
        self.combo_cat = ttk.Combobox(frame_saisie, values=["Alimentation", "Transport", "Loisirs", "Loyer", "Santé", "Autre"])
        self.combo_cat.grid(row=1, column=1, pady=5, sticky="we")
        self.combo_cat.current(0)

        tk.Label(frame_saisie, text="Montant (€):").grid(row=2, column=0, sticky="w")
        self.ent_montant = tk.Entry(frame_saisie)
        self.ent_montant.grid(row=2, column=1, pady=5, sticky="we")

        self.btn_ajouter = tk.Button(frame_saisie, text="Ajouter", command=self.ajouter_depense, bg="#4CAF50", fg="white")
        self.btn_ajouter.grid(row=3, columnspan=2, pady=10)

    
        frame_liste = tk.LabelFrame(self.root, text=" Historique des dépenses ", padx=10, pady=10)
        frame_liste.pack(padx=20, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_liste, columns=("Date", "Desc", "Cat", "Montant"), show='headings', height=8)
        self.tree.heading("Date", text="Date")
        self.tree.heading("Desc", text="Description")
        self.tree.heading("Cat", text="Catégorie")
        self.tree.heading("Montant", text="Montant (€)")
        
        self.tree.column("Date", width=80)
        self.tree.column("Montant", width=80)
        self.tree.pack(fill="both", expand=True)

      
        self.lbl_total = tk.Label(self.root, text="Total des dépenses : 0.00 €", font=("Arial", 12, "bold"))
        self.lbl_total.pack(pady=10)

    def ajouter_depense(self):
        """Logique pour enregistrer une dépense."""
        desc = self.ent_desc.get()
        cat = self.combo_cat.get()
        montant = self.ent_montant.get()
        from datetime import datetime
        date_actuelle = datetime.now().strftime("%d/%m/%Y")

        if not desc or not montant:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")
            return

        try:
           
            valeur = float(montant)
            
          
            with open(self.filename, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([date_actuelle, desc, cat, f"{valeur:.2f}"])
            
         
            self.tree.insert("", "end", values=(date_actuelle, desc, cat, f"{valeur:.2f} €"))
            self.calculer_total()
            
          
            self.ent_desc.delete(0, tk.END)
            self.ent_montant.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erreur", "Le montant doit être un nombre valide.")

    def charger_donnees(self):
        """Lit le fichier CSV pour remplir le tableau au démarrage."""
        total = 0
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.tree.insert("", "end", values=(row["Date"], row["Description"], row["Catégorie"], row["Montant"] + " €"))
            self.calculer_total()
        except Exception as e:
            print(f"Erreur de lecture : {e}")

    def calculer_total(self):
        """Calcule la somme de toutes les dépenses affichées."""
        total = 0.0
        for item in self.tree.get_children():
            valeur_str = self.tree.item(item)['values'][3] # Récupère la colonne Montant
            total += float(valeur_str.replace(' €', ''))
        self.lbl_total.config(text=f"Total des dépenses : {total:.2f} €")

if __name__ == "__main__":
    root = tk.Tk()
    app = EcoTrack(root)
    root.mainloop()
