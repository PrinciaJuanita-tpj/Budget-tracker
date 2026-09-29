import database
from datetime import datetime

def afficher_menu():
    """Affiche les options du menu principal dans le terminal."""
    print("MENU")
    print("1. Ajouter une dépense")
    print("2. Consulter les dépenses")
    print("3. Supprimer une dépense")
    print("4. Quitter")


def action_ajouter():
    """Demande les informations d'une dépense à l'utilisateur,

    l'enregistre en base de données et affiche une confirmation.
    """
    #obliger l'utilisateur à respecter le format de date
    while True :
        d = input("Date (AAAA-MM-JJ) : ")
        try:
            datetime.strptime(d, "%Y-%m-%d")
            break
        except ValueError:
            print("Date Invalide !")

            
    c = input("Catégorie (ex: Courses, Transport, Loyer) : ")

    #obliger l'utilisateur à ecrire un montant valide
    while True :    
        m = input("Montant (€) : ")
        try:
            m= float(m.replace(",","."))
            if m <= 0:
                print("Montant Invalide !")
            else:
                break
        except ValueError:
            print("Montant Invalide !")
    
    desc = input("Description (optionnel) : ")
    
    n = database.ajouter_depense(d,c,m,desc)
    
    print(f"Dépense n°{n} enregistrée avec succès !")
    


def action_consulter():
    """Demande un mois (AAAA-MM), récupère les totaux par catégorie

    et les affiche sous forme de récapitulatif clair.
    """
    #obliger l'utilisateur à respecter le format de date
    while True :
        d = input("Entrer l'année et le mois : (AAAA-MM) : ")
        try:
            datetime.strptime(d, "%Y-%m")
            break
        except ValueError:
            print("Date Invalide !")

    l = database.consulter_depenses(d) 
    
    if not l :
        print(f"Pas de dépenses à la date {d}")
    else :
        print(f"Dépenses du mois {d} : ")
        somme = 0
        for c,m in l :
            print(f"{c} : {m:.2f}€")
            somme = somme + m
        
        print(f"Dépenses totales pour {d} : {somme:.2f}€")


def action_supprimer():
    """
    Demande l'identifiant d'une dépense à supprimer,
    tente la suppression et informe l'utilisateur du résultat.
    """
    
    #obliger l'utilisateur à ecrire un id valide
    while True :    
        i = input("Identifiant de la dépenses : ")
        try:
            i = int(i)
            if i <= 0:
                print("ID Invalide !")
            else:
                break
        except ValueError:
            print("ID Invalide !")
    
   
    b = database.supprimer_depense(i)
    
    if b :
        print(f"Dépense n°{i} supprimée avec succès !")
    else :
        print(f"Aucune dépense de numero {i}")


def main():
    """
    Point d'entrée du programme : initialise la base de données
    et fait tourner la boucle interactive du menu.
    """
    print("Bienvenue dans Budget-tracker !")
    
    # Initialisation et garanti de l'existence de la base de donnée
    database.init_db() 
    
    while True:
        afficher_menu()
    
        choix = input()
        if choix == '1' :
            action_ajouter()
        elif choix == '2':
            action_consulter()
        elif choix == '3':
            action_supprimer()
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Option Invalide !")
        
if __name__ == "__main__":
    main()