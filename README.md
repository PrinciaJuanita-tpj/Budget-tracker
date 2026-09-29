# Budget-tracker


## Description

Application légère développée en Python permettant de suivre et d'analyser ses dépenses personnelles au quotidien à l'aide d'une base de données relationnelle locale SQLite. Elle propose au choix une interface graphique (GUI) interactive ou une interface en ligne de commande (CLI).

---

## 💡 Vision du Projet


* **Double interface au choix** : une interface graphique intuitive (`gui.py`) pour une gestion visuelle, ou une interface console rapide (`main.py`) pour les adeptes du terminal.

* **Architecture modulaire** : séparation stricte entre l'interface utilisateur (`main.py`) et la persistance des données (`database.py`).

* **Zéro dépendance externe** : exploitation des capacités natives de Python (`sqlite3`, `datetime`) sans framework tiers.

---

## 🎯 Fonctionnalités principales

1. **Ajouter une dépense** : saisie de la date, de la catégorie(Courses, cinéma etc...), du montant et d'une description.

2. **Consulter les dépenses** : affichage du montant total dépensé par catégorie pour un mois donné.

3. **Supprimer une dépense** : suppression d'une entrée à partir de son numéro d'identifiant (`id`).

4. **Lister toutes les dépenses** : 
Liste de toutes les dépenses de la plus récente à la plus anciennes.

---

## 🛠️ Stack Technique

- **Langage** : Python 3.14.7

- **Base de données** : SQLite (via le module standard `sqlite3`)

- **Interface graphique** : Tkinter / ttk (inclus dans la bibliothèque standard)

- **Interface console** : CLI interactive (terminal)

- **Versionnement** : Git & GitHub

---

## 📂 Architecture du Projet

```text
Budget-tracker/
│
├── .gitignore         # Fichiers exclus du versionnement (*.db, __pycache__)
├── README.md          # Documentation du projet
├── database.py        # Logique d'accès aux données et requêtes SQL
├── gui.py             # Interface graphique utilisateur (Tkinter)
└── main.py            # Point d'entrée de l'application console (CLI)
```
---

## 🖥️ Aperçu de l'Expérience Utilisateur

```text
===Budget-tracker===
1. Ajouter une dépense
2. Consulter les dépenses
3. Supprimer une dépense
4. Lister toutes les dépenses
5. Quitter

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
   * **Version graphique :**
     ```bash
     python gui.py
     ```
   * **Version console :**
     ```bash
     python main.py
     ```