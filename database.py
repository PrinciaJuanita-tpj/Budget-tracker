import sqlite3

# Nom du fichier qui stocke la base de données sur l'ordinateur
DB_NAME = "budget.db"


def init_db():
    """
    Initialise la base de données.
    Crée la table 'depenses' si elle n'existe pas encore.
    """
    
    # 1. On ouvre le fichier de la base (il se crée tout seul s'il n'existe pas)
    conn = sqlite3.connect(DB_NAME)

    # 2. Le curseur sert d'outil pour taper et lancer les requêtes SQL
    cursor = conn.cursor()

    # 3. On crée la table 'depenses' si elle n'est pas déjà présente
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS depenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Numéro unique géré tout seul
            date TEXT NOT NULL,                   -- Date au format AAAA-MM-JJ
            categorie TEXT NOT NULL,              -- Ex: Courses, Loyer, Loisirs
            montant REAL NOT NULL,                -- Prix en euros (nombre à virgule)
            description TEXT                      -- Petit mot explicatif (optionnel)
        )
    """)

    # 4. On valide l'enregistrement des modifications sur le disque
    conn.commit()

    # 5. On referme la connexion pour libérer le fichier
    conn.close()
    
def ajouter_depense(date,categorie,montant,description=""):
    """
    Insère une nouvelle dépense dans la base de données.

    Paramètres :
        date (str) : Date de l'opération au format 'AAAA-MM-JJ'
        categorie (str) : Catégorie associée (ex: 'Alimentation', 'Transport')
        montant (float) : Montant payé
        description (str, optionnel) : Détail ou note sur la dépense

    Retourne :
        int : L'identifiant unique (id) attribué à la ligne insérée.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO depenses (date,categorie,montant,description)
        VALUES (?, ?, ?, ?)
    """,
        (date,categorie,montant,description),
        )#Insère les valeurs que l'utilisateur devra entrer dans la table

    conn.commit()
    nouvel_id = cursor.lastrowid #récupère le numéro d'identifiant (id) que SQLite vient tout juste de générer automatiquement
    conn.close()
    return nouvel_id

def supprimer_depense(d_id):
    """
    Supprime une dépense existante à partir de son identifiant.
    
    Paramètre :
        id (int) : L'id de la dépense à supprimer
        
    Retourne :
        bool : True si la ligne a bien été supprimée, False si l'id n'existait pas.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM depenses
        WHERE id = ?
    """,(d_id,)
        ) #supprime la ligne de la table

    conn.commit()
    lignes_Affectees = cursor.rowcount #recupère nombre de lignes affectées par la suppression
    conn.close()
    if lignes_Affectees == 0: #verifie la suppression
        return False
    else:
        return True

def consulter_depenses(annee_mois):
    """Calcule le montant total dépensé par catégorie pour un mois donné.

    Paramètre :
        annee_mois (str) : Mois ciblé au format 'AAAA-MM' (ex: '2026-09')

    Retourne :
        list[tuple[str, float]] : Liste de tuples contenant chacun la catégorie
        et la somme dépensée (ex: [('Courses', 120.5), ('Loisirs', 45.0)]).
        Retourne une liste vide si aucune dépense n'est trouvée.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
    """
        SELECT categorie, SUM(montant)
        FROM depenses
        WHERE date LIKE ?
        GROUP BY categorie
    """, (annee_mois+"%",)
        ) #filtre
    lignes = cursor.fetchall() #toutes les lignes trouvées par le filtre
    conn.close()
    return lignes

def lister_toutes_depenses():
    """
    Récupère l'ensemble des dépenses enregistrées en base,
    triées de la plus récente à la plus ancienne.

    Retourne :
        list[tuple] : Liste de tuples contenant (id, date, categorie, montant, description).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
    """
        SELECT *
        FROM depenses
        ORDER BY date DESC
    """, ) 
    lignes = cursor.fetchall() #toutes les lignes trouvées par le filtre
    conn.close()
    return lignes
    