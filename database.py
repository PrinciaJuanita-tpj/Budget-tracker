import sqlite3

# Nom du fichier qui stocke la base de données sur l'ordinateur
DB_NAME = "budget.db"


def init_db():
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