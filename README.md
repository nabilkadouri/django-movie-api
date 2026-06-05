# CineVault API

API REST développée avec Django et Django REST Framework permettant la gestion de films, catégories, acteurs, réalisateurs, reviews et favoris.

Ce projet a été réalisé dans une logique d’apprentissage avancé du backend Django REST afin de maîtriser :

* Architecture REST
* Django REST Framework
* Serializers
* Validations métier
* Authentification JWT
* Permissions utilisateurs
* Relations SQL
* CRUD personnalisés
* Organisation d’un backend professionnel

---

# Fonctionnalités

## Authentification JWT

* Inscription utilisateur
* Connexion utilisateur
* Génération Access Token
* Génération Refresh Token
* Protection des routes privées

## Movies

* Création d’un film
* Liste des films
* Détail d’un film
* Modification partielle d’un film
* Remplacement complet d’un film
* Suppression d’un film

## Categories

* Création d’une catégorie
* Liste des catégories
* Modification d’une catégorie
* Suppression d’une catégorie

## Directors

* Création d’un réalisateur
* Liste des réalisateurs
* Détail d’un réalisateur
* Suppression d’un réalisateur

## Actors

* Création d’un acteur
* Liste des acteurs
* Détail d’un acteur
* Suppression d’un acteur

## Reviews

* Création d’une review
* Liste des reviews
* Détail d’une review
* Modification d’une review
* Suppression d’une review

## Favorites

* Ajout d’un film en favori
* Liste des favoris d’un utilisateur
* Détail d’un favori
* Suppression d’un favori

---

# Stack technique

* Python 3
* Django
* Django REST Framework
* Simple JWT
* SQLite
* Postman

---

# Architecture

```txt
movies/
├── models/
│   ├── movie_model.py
│   ├── category_model.py
│   ├── actor_model.py
│   ├── director_model.py
│   ├── review_model.py
│   └── favorite_model.py
│
├── serializers/
│   ├── movie_serializer.py
│   ├── review_serializer.py
│   ├── favorite_serializer.py
│   ├── actor_serializer.py
│   ├── director_serializer.py
│   └── ...
│
├── permissions/
│   ├── review_permissions.py
│   ├── favorite_permissions.py
│
├── views/
│   ├── movie_views.py
│   ├── review_views.py
│   ├── favorite_views.py
│   ├── actor_views.py
│   └── director_views.py
│
├── admin.py
├── urls.py
```

---

# Relations SQL

## Movie

* ManyToMany → Categories
* ManyToMany → Actors
* ForeignKey → Director

## Favorite

* ForeignKey → User
* ForeignKey → Movie

## Review

* ForeignKey → User
* ForeignKey → Movie

---

# Règles métier

## Reviews

* Un utilisateur ne peut publier qu'une seule review par film
* Une note doit être comprise entre 1 et 10
* Les commentaires sont automatiquement nettoyés

## Favorites

* Un utilisateur ne peut ajouter qu'une seule fois un film dans ses favoris

## Movies

* Une année de sortie ne peut pas être supérieure à l'année actuelle
* Les données textuelles sont nettoyées avant sauvegarde

## Permissions

* Les reviews ne peuvent être modifiées ou supprimées que par leur propriétaire
* Les favoris ne peuvent être supprimés que par leur propriétaire
* Les acteurs et réalisateurs sont réservés aux administrateurs

---

# Authentification JWT

## Register

```http
POST /api/auth/register/
```

## Login

```http
POST /api/auth/login/
```

Réponse :

```json
{
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token"
}
```

## Refresh Token

```http
POST /api/auth/token/refresh/
```

---

# Endpoints API

## Movies

| Méthode | Endpoint          |
| ------- | ----------------- |
| GET     | /api/movies/      |
| POST    | /api/movies/      |
| GET     | /api/movies/<id>/ |
| PATCH   | /api/movies/<id>/ |
| PUT     | /api/movies/<id>/ |
| DELETE  | /api/movies/<id>/ |

---

## Categories

| Méthode | Endpoint                     |
| ------- | ---------------------------- |
| GET     | /api/movies/categories/      |
| POST    | /api/movies/categories/      |
| PATCH   | /api/movies/categories/<id>/ |
| DELETE  | /api/movies/categories/<id>/ |

---

## Directors

| Méthode | Endpoint                    |
| ------- | --------------------------- |
| GET     | /api/movies/directors/      |
| POST    | /api/movies/directors/      |
| GET     | /api/movies/directors/<id>/ |
| DELETE  | /api/movies/directors/<id>/ |

---

## Actors

| Méthode | Endpoint                 |
| ------- | ------------------------ |
| GET     | /api/movies/actors/      |
| POST    | /api/movies/actors/      |
| GET     | /api/movies/actors/<id>/ |
| DELETE  | /api/movies/actors/<id>/ |

---

## Reviews

| Méthode | Endpoint                  |
| ------- | ------------------------- |
| GET     | /api/movies/reviews/      |
| POST    | /api/movies/reviews/      |
| GET     | /api/movies/reviews/<id>/ |
| PATCH   | /api/movies/reviews/<id>/ |
| DELETE  | /api/movies/reviews/<id>/ |

---

## Favorites

| Méthode | Endpoint                    |
| ------- | --------------------------- |
| GET     | /api/movies/favorites/      |
| POST    | /api/movies/favorites/      |
| GET     | /api/movies/favorites/<id>/ |
| DELETE  | /api/movies/favorites/<id>/ |

---

# Django Admin

Le projet utilise l'interface d'administration Django pour gérer les données.

Accès :

```http
http://127.0.0.1:8000/admin/
```

Fonctionnalités :

* Consultation des films
* Consultation des acteurs
* Consultation des réalisateurs
* Consultation des reviews
* Consultation des favoris
* Consultation des utilisateurs

Les identifiants sont affichés directement dans l'interface afin de faciliter les tests API.

---

# Tests Postman

L'ensemble des endpoints a été testé avec Postman.

Tests réalisés :

* Authentification JWT
* CRUD Movies
* CRUD Reviews
* CRUD Favorites
* CRUD Actors
* CRUD Directors
* Permissions utilisateurs
* Validation des données métier

Ajouter une capture d'écran :

```txt
docs/postman-tests.png
```

Puis dans le README :

```md
![Postman Collection](docs/postman-tests.png)
```

---

# Installation

## Cloner le projet

```bash
git clone https://github.com/NabilKADOURI/cinevault.git
```

## Créer un environnement virtuel

```bash
python3 -m venv .venv
```

## Activer l'environnement

### Mac / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## Installer les dépendances

```bash
pip install -r requirements.txt
```

## Appliquer les migrations

```bash
python manage.py migrate
```

## Créer un super utilisateur

```bash
python manage.py createsuperuser
```

## Lancer le serveur

```bash
python manage.py runserver
```

---

# Exemple JSON Movie

```json
{
    "title": "Interstellar",
    "description": "Science fiction movie",
    "release_year": 2014,
    "duration": 169,
    "image": "https://image-url.com",
    "is_published": true,
    "director": 1,
    "categories": [1, 2],
    "actors": [1, 2, 3]
}
```

---

# Objectifs pédagogiques

Ce projet a été réalisé afin de travailler :

* Django REST Framework
* JWT Authentication
* Permissions DRF
* APIView
* CRUD personnalisés
* Relations SQL
* Validations métier
* Serializer Context
* Ownership Validation
* Architecture REST
* Structuration backend professionnelle
* Tests Postman

---

# Améliorations futures

* PATCH Director
* PATCH Actor
* Pagination
* Recherche et filtres
* Upload d’images
* Documentation Swagger / OpenAPI
* Tests unitaires
* Dockerisation
* Déploiement Cloud

---

# Auteur

**Nabil KADOURI**

Développeur Web & Web Mobile
Formation Concepteur Développeur d'Applications
