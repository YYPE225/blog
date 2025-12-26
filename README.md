
* **Nom GitHub** : `YYPE225`
* **Nom complet** : `YAPI YAPO PAUL EMMANUEL`
* **Repo** : `mesprojets`
* **Projet 2** (blog)


---

# 📝 README — Projet 2

# Blog — Application web Django

## Description

Application web de type **blog** développée avec **Django**, permettant aux utilisateurs de s’inscrire, se connecter et interagir avec du contenu publié.

Les utilisateurs authentifiés peuvent :

* créer des articles,
* commenter les articles,
* modifier et supprimer uniquement leurs propres contenus.

Ce projet a été réalisé dans un objectif **d’apprentissage progressif de Django** et de **constitution d’un portfolio professionnel**.

---

## Fonctionnalités

* Inscription et authentification des utilisateurs
* Création, modification et suppression d’articles (CRUD complet)
* Ajout, modification et suppression de commentaires
* Gestion des permissions utilisateurs
* Pagination des articles
* Recherche par titre
* Interface web en HTML/CSS (sans framework frontend)
* Interface d’administration Django
* Déploiement sur PythonAnywhere

---

## Technologies utilisées

* Python
* Django
* HTML5
* CSS3
* SQLite (développement)
* Git & GitHub
* PythonAnywhere (déploiement)

---

## Installation et exécution en local

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/YYPE225/mesprojets.git
cd projet2
```

---

### 2️⃣ Créer et activer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS
```

---

### 3️⃣ Installer les dépendances

```bash
pip install django
```

---

### 4️⃣ Appliquer les migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Créer un superutilisateur

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Lancer le serveur

```bash
python manage.py runserver
```

---

### 7️⃣ Accéder à l’application

* Site : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Administration : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Structure du projet

```
blog_project/
├── articles/
├── users/
├── templates/
├── static/
├── manage.py
└── README.md
```

---

## Déploiement

Le projet est déployé sur **PythonAnywhere** et accessible via une URL publique.

---

## Compétences démontrées

* Architecture d’un projet Django
* Modélisation de base de données relationnelle
* Authentification et gestion des permissions
* CRUD avancé (articles et commentaires)
* Pagination et recherche
* Templates Django
* Gestion des fichiers statiques
* Déploiement d’une application Django
* Utilisation de Git et GitHub

---

## Auteur

**YAPI YAPO PAUL EMMANUEL**
GitHub : [https://github.com/YYPE225](https://github.com/YYPE225)

---



---


