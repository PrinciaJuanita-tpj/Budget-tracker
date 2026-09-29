# Budget-tracker


## Description

Application console légère développée en Python permettant de suivre et d'analyser ses dépenses personnelles au quotidien à l'aide d'une base de données relationnelle locale SQLite.

---

## 💡 Vision du Projet


* **Exécution directe au clavier** : une interface en ligne de commande claire pour saisir ses dépenses en quelques secondes sans ouvrir un tableur lourd.

* **Architecture modulaire** : séparation stricte entre l'interface utilisateur (`main.py`) et la persistance des données (`database.py`).

* **Zéro dépendance externe** : exploitation des capacités natives de Python (`sqlite3`, `datetime`) sans framework tiers.

---

## 🎯 Fonctionnalités principales

1. **Ajouter une dépense** : saisie de la date, de la catégorie(Courses, cinéma etc...), du montant et d'une description.

2. **Consulter les dépenses** : affichage du montant total dépensé par catégorie pour un mois donné.

3. **Supprimer une dépense** : suppression d'une entrée à partir de son numéro d'identifiant (`id`).

---

## 🛠️ Stack Technique

- **Langage** : Python 3.14.7
- **Base de données** : SQLite (via le module standard `sqlite3`)
- **Interface** : Ligne de commande 
- **Versionnement** : Git & GitHub

---

## 📂 Architecture du Projet

```text
Budget-tracker/
│
├── .gitignore        # Fichiers exclus du versionnement (*.db, __pycache__)
├── README.md         # Documentation du projet
├── database.py       # Logique d'accès aux données et requêtes SQL
└── main.py           # Point d'entrée de l'application et menu interactif
```
---

## 🖥️ Aperçu de l'Expérience Utilisateur

```text
===Budget-tracker===
1. Ajouter une dépense
2. Consulter les dépenses
3. Supprimer une dépense
4. Quitter

--- Nouvelle dépense ---
Date (AAAA-MM-JJ, Entrée pour aujourd'hui) : 2026-09-29
Catégorie (ex: Courses, Transport, Loyer) : Courses
Montant (€) : 42.50
Description : Courses de la semaine chez Lidl
✅ Dépense enregistrée avec succès (ID: 1)
```

---

## 🚀 Lancement Rapide

1. Cloner le projet sur votre machine

2. Lancer l'application :
   ```bash
     python main.py
    ```