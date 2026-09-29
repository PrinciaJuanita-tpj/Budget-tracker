import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import database


#initialisation et garantie de l'existence de la base de données
database.init_db()

root = tk.Tk()
root.title("Budget Tracker")

l1 = ttk.Label(root, text="Bienvenue dans Budget Tracker", font=("Arial", 12,"bold"))
l1.pack(pady=10)

l2 = ttk.Label(root, text="_Suivi et gestion de vos dépenses_", font=("Arial", 11))
l2.pack(pady=10)

# --- Formulaire d'ajout d'une dépense ---
cadre = ttk.LabelFrame(root, text="[+] Nouvelle dépense")
cadre.pack(fill="x", padx=15, pady=10)

# Date
l_date = ttk.Label(cadre, text="Date :")
l_date.grid(row=0, column=0, sticky="w", padx=10, pady=5)

# Conteneur pour aligner les 3 listes déroulantes
cadre_date = ttk.Frame(cadre)
cadre_date.grid(row=0, column=1, sticky="w", padx=10, pady=5)

# Jours (01 à 31)
jours = [f"{i:02d}" for i in range(1, 32)]
combo_jour = ttk.Combobox(cadre_date, values=jours, state="readonly", width=4)
combo_jour.pack(side="left", padx=(0, 4))

# Mois (01 à 12)
mois = [f"{i:02d}" for i in range(1, 13)]
combo_mois = ttk.Combobox(cadre_date, values=mois, state="readonly", width=4)
combo_mois.pack(side="left", padx=(0, 4))

# Années (2000 à 2040)
annee_courante = datetime.now().year
annees = [str(a) for a in range(2000, annee_courante + 15)]
combo_annee = ttk.Combobox(cadre_date, values=annees, state="readonly", width=6)
combo_annee.pack(side="left")

# Valeurs sélectionnées par défaut (date d'aujourd'hui)
ajd = datetime.now()
combo_jour.set(f"{ajd.day:02d}")
combo_mois.set(f"{ajd.month:02d}")
combo_annee.set(str(ajd.year))


# Catégorie
categories = [
    "Alimentation & Courses",
    "Logement & Charges",
    "Transport",
    "Santé & Soins",
    "Loisirs & Sorties",
    "Shopping & Perso",
    "Abonnements",
    "Dettes & Prêts",
    "Autre",
]

l_categorie = ttk.Label(cadre, text="Catégorie :")
l_categorie.grid(row=1, column=0, sticky="w", padx=10, pady=5)

combo_cat = ttk.Combobox(cadre, values=categories, state="readonly", width=28)
combo_cat.grid(row=1, column=1, sticky="w", padx=10, pady=5)
combo_cat.current(0)  # Sélectionne "Alimentation & Courses" par défaut

# Montant
l_montant = ttk.Label(cadre, text="Montant (€) :")
l_montant.grid(row=2, column=0, sticky="w", padx=10, pady=5)

e_montant = ttk.Entry(cadre, width=30)
e_montant.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Description
l_description = ttk.Label(cadre, text="Description :")
l_description.grid(row=3, column=0, sticky="w", padx=10, pady=5)

e_description = ttk.Entry(cadre, width=30)
e_description.grid(row=3, column=1, sticky="w", padx=10, pady=5)

# Bouton Ajouter
bouton_ajouter = ttk.Button(cadre, text="Ajouter la dépense")
bouton_ajouter.grid(row=4, column=0, columnspan=2, pady=10)


# --- Filtrage par période et catégorie ---
cadreF = ttk.LabelFrame(root, text="Filtrer les dépenses")
cadreF.pack(fill="x", padx=15, pady=5)

# --- Listes avec choix vide pour laisser le critère libre ---
jours_filtre = [""] + [f"{i:02d}" for i in range(1, 32)]
mois_filtre = [""] + [f"{i:02d}" for i in range(1, 13)]
annee_courante = datetime.now().year
annees_filtre = [""] + [str(a) for a in range(2020, annee_courante + 6)]

# Label et conteneur date
l_date_f = ttk.Label(cadreF, text="Date (J / M / A) :")
l_date_f.grid(row=0, column=0, sticky="w", padx=5, pady=5)

cadre_f_date = ttk.Frame(cadreF)
cadre_f_date.grid(row=0, column=1, sticky="w", padx=5, pady=5)

combo_f_jour = ttk.Combobox(
    cadre_f_date, values=jours_filtre, state="readonly", width=3
)
combo_f_jour.pack(side="left", padx=(0, 2))

combo_f_mois = ttk.Combobox(
    cadre_f_date, values=mois_filtre, state="readonly", width=3
)
combo_f_mois.pack(side="left", padx=(0, 2))

combo_f_annee = ttk.Combobox(
    cadre_f_date, values=annees_filtre, state="readonly", width=5
)
combo_f_annee.pack(side="left")

# Catégorie
l_filtre_cat = ttk.Label(cadreF, text="Catégorie :")
l_filtre_cat.grid(row=0, column=2, sticky="w", padx=5, pady=5)

combo_filtre_cat = ttk.Combobox(
    cadreF, values=["Toutes"] + categories, state="readonly", width=16
)
combo_filtre_cat.grid(row=0, column=3, padx=5, pady=5)
combo_filtre_cat.current(0)

# Boutons d'action
bouton_filtrer = ttk.Button(cadreF, text="Filtrer")
bouton_filtrer.grid(row=0, column=4, padx=6, pady=5)

bouton_reinit = ttk.Button(cadreF, text="Réinitialiser")
bouton_reinit.grid(row=0, column=5, padx=5, pady=5)

# --- Tableau des dépenses---
cadre_tableau = ttk.LabelFrame(root, text="Historique des dépenses")
cadre_tableau.pack(fill="both", expand=True, padx=15, pady=5)

# Colonnes du tableau
colonnes = ("id", "date", "categorie", "montant", "description")
tableau = ttk.Treeview(cadre_tableau, columns=colonnes, show="headings", height=8)

# Configuration des titres des colonnes
tableau.heading("id", text="ID")
tableau.heading("date", text="Date")
tableau.heading("categorie", text="Catégorie")
tableau.heading("montant", text="Montant (€)")
tableau.heading("description", text="Description")

# Configuration des largeurs et alignements
tableau.column("id", width=40, anchor="center")
tableau.column("date", width=90, anchor="center")
tableau.column("categorie", width=140, anchor="w")
tableau.column("montant", width=80, anchor="e")
tableau.column("description", width=220, anchor="w")

# Barre de défilement verticale
scrollbar = ttk.Scrollbar(cadre_tableau, orient="vertical", command=tableau.yview)
tableau.configure(yscrollcommand=scrollbar.set)

# Positionnement du tableau et de la scrollbar côte à côte
tableau.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)


# --- Barre d'actions et récapitulatif ---
cadre_bas = ttk.Frame(root)
cadre_bas.pack(fill="x", padx=15, pady=10)

# Bouton de suppression (à gauche)
bouton_supprimer = ttk.Button(cadre_bas, text="Supprimer la sélection")
bouton_supprimer.pack(side="left")

# Label du total (à droite)
l_total = ttk.Label(cadre_bas, text="Total affiché : 0.00 €", font=("Arial", 10, "bold"))
l_total.pack(side="right")

# --- Fonctions ---
def charger_tableau(depenses=None):
    """
    Actualise l'affichage du Treeview et recalcule le montant total.
    Vide les lignes actuellement affichées dans le tableau, insère les
    dépenses fournies (ou récupère l'ensemble des dépenses depuis la base de
    données si aucun argument n'est transmis), puis met à jour le label
    affichant la somme totale.
    Args:
        depenses (list of tuple, optional): Liste de tuples représentant les
            enregistrements de dépenses (id, date, categorie, montant, description).
            Par défaut None, ce qui déclenche une lecture complète via database.
    """
    # Si aucune liste n'est fournie, on récupère toutes les dépenses en base
    if depenses is None:
        depenses = database.lister_toutes_depenses()
        
    # Nettoyage : on supprime toutes les lignes actuelles du Treeview (pout le filtrage)
    for item in tableau.get_children():
        tableau.delete(item)
        
    # Compteur pour la somme totale des dépenses affichées
    total = 0.0
    
    # Parcours des enregistrements et insertion dans le tableau
    for depense in depenses:
        # depense est un tuple : (id, date, categorie, montant, description)
        tableau.insert("", "end", values=depense)

        # On additionne le montant (index 3 du tuple)
        try:
            total += float(depense[3])
        except (ValueError, TypeError):
            pass
        
    # Mise à jour dynamique de total
    l_total.config(text=f"Total affiché : {total:.2f} €")



def ajouter_depense_gui():
    """Récupère les saisies du formulaire, valide les données et insère la dépense."""
    # 1. Reconstitution de la date au format AAAA-MM-JJ
    j = combo_jour.get().strip()
    m = combo_mois.get().strip()
    a = combo_annee.get().strip()
    date = f"{a}-{m}-{j}"

    # Vérification de l'existence réelle de la date (ex. 31 février, 31 avril)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror(
            "Date invalide",
            f"La date {j}/{m}/{a} n'existe pas dans le calendrier.",
        )
        return

    categorie = combo_cat.get().strip()
    montant_str = e_montant.get().strip()
    description = e_description.get().strip()

    # 2. Vérification de présence du montant
    if not montant_str:
        messagebox.showerror(
            "Erreur de saisie", "Le montant est obligatoire."
        )
        return

    # 3. Validation numérique du montant (> 0)
    try:
        montant = float(montant_str.replace(",", "."))
        if montant <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Erreur de montant", "Le montant doit être un nombre positif valide."
        )
        return

    # 4. Insertion dans SQLite via le module database
    database.ajouter_depense(date, categorie, montant, description)

    # 5. Actualisation de l'affichage
    charger_tableau()

    # 6. Réinitialisation des champs pour la saisie suivante
    e_montant.delete(0, "end")
    e_description.delete(0, "end")
    combo_cat.current(0)

    # Remise du focus sur la sélection du jour
    combo_jour.focus_set()

# Lier la fonction au bouton 
bouton_ajouter.config(command=ajouter_depense_gui)


def supprimer_depense_gui():
    """Supprime une ou plusieurs dépenses sélectionnées dans le Treeview."""
    selection = tableau.selection()

    # Vérification : y a-t-il au moins un élément sélectionné ?
    if not selection:
        messagebox.showwarning(
            "Aucune sélection",
            "Veuillez sélectionner au moins une dépense à supprimer.",
        )
        return

    nb_elements = len(selection)

    # Message de confirmation adapté au nombre de lignes
    if nb_elements == 1:
        valeurs = tableau.item(selection[0], "values")
        id_depense = valeurs[0]
        desc = valeurs[4] if len(valeurs) > 4 else ""
        msg = f"Voulez-vous vraiment supprimer la dépense n°{id_depense} ({desc}) ?"
    else:
        msg = f"Voulez-vous vraiment supprimer ces {nb_elements} dépenses ?"

    confirmation = messagebox.askyesno("Confirmation", msg)
    if not confirmation:
        return

    # Parcours et suppression de chaque ligne sélectionnée
    for item_id in selection:
        valeurs = tableau.item(item_id, "values")
        id_depense = valeurs[0]
        database.supprimer_depense(id_depense)

    # Actualisation globale du tableau et du total
    charger_tableau()
    
bouton_supprimer.config(command=supprimer_depense_gui)


def construire_date_filtre(j, m, a, libelle):
    """Vérifie et assemble une date de filtre si au moins un champ est renseigné."""
    # Si tous les champs sont vides, aucun filtre sur cette borne
    if not j and not m and not a:
        return None

    # Si l'un des trois champs manque
    if not (j and m and a):
        messagebox.showerror(
            "Date incomplète",
            f"Veuillez sélectionner le jour, le mois et l'année pour la date de {libelle}.",
        )
        return False

    date_str = f"{a}-{m}-{j}"
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        messagebox.showerror(
            "Date invalide",
            f"La date de {libelle} ({j}/{m}/{a}) n'existe pas dans le calendrier.",
        )
        return False


def appliquer_filtre_gui():
    """Applique le filtre avec n'importe quelle combinaison de jour, mois, année et catégorie."""
    j = combo_f_jour.get().strip()
    m = combo_f_mois.get().strip()
    a = combo_f_annee.get().strip()
    cat = combo_filtre_cat.get().strip()

    resultats = database.filtrer_depenses(
        annee=a or None,
        mois=m or None,
        jour=j or None,
        categorie=cat if cat != "Toutes" else None,
    )
    charger_tableau(resultats)


def reinitialiser_filtre_gui():
    """Remet à zéro tous les critères du filtre."""
    combo_f_jour.set("")
    combo_f_mois.set("")
    combo_f_annee.set("")
    combo_filtre_cat.current(0)
    charger_tableau()        
bouton_filtrer.config(command=appliquer_filtre_gui)
bouton_reinit.config(command=reinitialiser_filtre_gui)

# Entrée dans Date -> envoie vers Catégorie
combo_jour.bind("<Return>", lambda event: combo_mois.focus_set())
combo_mois.bind("<Return>", lambda event: combo_annee.focus_set())
combo_annee.bind("<Return>", lambda event: combo_cat.focus_set())

# Entrée dans Catégorie -> envoie vers Montant
combo_cat.bind("<Return>", lambda event: e_montant.focus_set())

# Entrée dans Montant -> envoie vers Description
e_montant.bind("<Return>", lambda event: e_description.focus_set())

# Entrée dans Description (dernier champ) -> valide et ajoute la dépense
e_description.bind("<Return>", lambda event: ajouter_depense_gui())

combo_f_jour.bind("<Return>", lambda event: combo_f_mois.focus_set())
combo_f_mois.bind("<Return>", lambda event: combo_f_annee.focus_set())
combo_f_annee.bind("<Return>", lambda event: combo_filtre_cat.focus_set())
combo_filtre_cat.bind("<Return>", lambda event: appliquer_filtre_gui())
combo_filtre_cat.bind("<Return>", lambda event: appliquer_filtre_gui())


if __name__ == "__main__":
    charger_tableau()
    root.mainloop()