# Django Movie API

API REST développée avec Django et Django REST Framework permettant la gestion de films, catégories, acteurs, réalisateurs, reviews et favoris.

Ce projet a été réalisé dans une logique d’apprentissage avancé du backend Django REST :

- architecture REST
- serializers DRF
- relations SQL
- validations métier
- CRUD personnalisés
- organisation backend

---

# Fonctionnalités

## Movies

- Création d’un film
- Liste des films
- Détail d’un film
- Modification partielle d’un film
- Remplacement complet d’un film
- Suppression d’un film

## Categories

- Création d’une catégorie
- Liste des catégories
- Modification d’une catégorie
- Suppression d’une catégorie

## Directors

- Création d’un réalisateur
- Liste des réalisateurs
- Détail d’un réalisateur
- Suppression d’un réalisateur

## Actors

- Création d’un acteur
- Liste des acteurs
- Détail d’un acteur
- Suppression d’un acteur

## Reviews

- Création d’une review
- Liste des reviews
- Détail d’une review
- Modification d’une review
- Suppression d’une review

## Favorites

- Ajout d’un film en favori
- Liste des favoris
- Suppression d’un favori

---

# Stack technique

- Python
- Django
- Django REST Framework
- SQLite

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
│   └── ...
│
├── views/
│   ├── movie_views.py
│   ├── review_views.py
│   ├── favorite_views.py
│   └── ...
│
├── services/
│
├── urls.py
```

---

# Relations SQL

## Movie

- ManyToMany → Categories
- ManyToMany → Actors
- ForeignKey → Director

## Favorite

- ForeignKey → User
- ForeignKey → Movie

## Review

- ForeignKey → User
- ForeignKey → Movie

---

# Règles métier

- Un utilisateur ne peut pas ajouter deux fois le même film en favori
- Un utilisateur ne peut pas poster plusieurs reviews pour un même film
- Une review doit avoir une note comprise entre 1 et 10
- Une année de film ne peut pas être supérieure à l’année actuelle
- Les champs texte sont nettoyés automatiquement via les serializers

---

# Endpoints API

## Movies

| Méthode | Endpoint | Description |
|---|---|---|
| GET | /movies/ | Liste des films |
| POST | /movies/ | Ajouter un film |
| GET | /movies/<id>/ | Détail d’un film |
| PATCH | /movies/<id>/ | Modifier partiellement un film |
| PUT | /movies/<id>/ | Remplacer complètement un film |
| DELETE | /movies/<id>/ | Supprimer un film |

---

## Categories

| Méthode | Endpoint | Description |
|---|---|---|
| GET | /categories/ | Liste des catégories |
| POST | /categories/ | Ajouter une catégorie |
| PATCH | /categories/<id>/ | Modifier une catégorie |
| DELETE | /categories/<id>/ | Supprimer une catégorie |

---

## Directors

| Méthode | Endpoint | Description |
|---|---|---|
| GET | /directors/ | Liste des réalisateurs |
| POST | /directors/ | Ajouter un réalisateur |
| GET | /directors/<id>/ | Détail d’un réalisateur |
| DELETE | /directors/<id>/ | Supprimer un réalisateur |

---

## Actors

| Méthode | Endpoint | Description |
|---|---|---|
| GET | /actors/ | Liste des acteurs |
| POST | /actors/ | Ajouter un acteur |
| GET | /actors/<id>/ | Détail d’un acteur |
| DELETE | /actors/<id>/ | Supprimer un acteur |

---

## Reviews

| Méthode | Endpoint | Description |
|---|---|---|
| GET | /reviews/ | Liste des reviews |
| POST | /reviews/ | Ajouter une review |
| GET | /reviews/<id>/ | Détail d’une review |
| PATCH | /reviews/<id>/ | Modifier une review |
| DELETE | /reviews/<id>/ | Supprimer une review |

---

## Favorites

| Méthode | Endpoint | Description |
|---|---|---|
| GET | /favorites/ | Liste des favoris |
| POST | /favorites/ | Ajouter un favori |
| DELETE | /favorites/<id>/ | Supprimer un favori |

---

# Installation

## Cloner le projet

```bash
git clone https://github.com/TON-USERNAME/django-movie-api.git
```

---

## Créer un environnement virtuel

```bash
python3 -m venv venv
```

---

## Activer le venv

### Mac / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Appliquer les migrations

```bash
python manage.py migrate
```

---

## Créer un super utilisateur

```bash
python manage.py createsuperuser
```

---

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

- Django REST Framework
- Architecture REST
- CRUD personnalisés
- Relations SQL
- Validations métier
- Structuration backend
- Gestion des serializers
- Gestion des endpoints API
- Réflexion architecture backend

---

# Améliorations futures

- Authentification JWT
- Permissions utilisateurs
- Pagination
- Recherche et filtres
- Upload d’images
- Documentation Swagger/OpenAPI
- Tests unitaires
- Dockerisation

---

# Auteur

Nabil KADOURI