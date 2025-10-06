# 🎵 Music Library (Python + MySQL)

A **Music Library REST API** built using **Flask** and **MySQL**, designed for intermediate-level developers to manage artists, albums, tracks, and playlists. This project demonstrates RESTful API design, database operations, and practical SQL usage without relying on an ORM, making it an excellent learning resource and a lightweight backend for music-related applications.

---

## 📝 Overview

This project provides a backend API to manage a music library with the following capabilities:

- Maintain a catalog of **artists**, **albums**, and **tracks**.
- Create, read, update, and delete (CRUD) operations for all entities.
- Build and manage **playlists**, including adding tracks dynamically.
- Search functionality to filter tracks by **title, artist, or album**.
- Paginated endpoints for scalable retrieval of large datasets.
- Uses explicit SQL queries via **mysql-connector-python**, making it easy to understand SQL interactions.
- Optional Docker setup for running MySQL and the Flask app with minimal configuration.

---

## 🚀 Features

### Core Features
- **Artists**
  - List all artists, create new artists.
  - Search and pagination support.
- **Albums**
  - Create and list albums, link albums to artists.
- **Tracks**
  - Full CRUD for tracks.
  - Search by title, artist, or album.
  - View detailed track information by ID.
- **Playlists**
  - Create playlists, add tracks, list all playlists.
  - Retrieve playlist details including all tracks.
- **Database**
  - Sample schema and seed data included.
  - Explicit SQL usage for learning purposes.
- **Pagination**
  - Supports `?page=` and `?per_page=` query parameters for list endpoints.

### Additional Features
- Lightweight, no heavy dependencies.
- Easy to extend with authentication, advanced filtering, or a front-end.
- Docker support for MySQL + Flask containerization.

---

## ⚙️ Requirements

- Python 3.9+
- MySQL Server or MariaDB
- Python packages:
  ```text
  flask
  mysql-connector-python
  python-dotenv

## 🌐 API Endpoints

| Method | Endpoint                 | Description                                   |
|--------|--------------------------|-----------------------------------------------|
| GET    | `/artists`               | List all artists (supports pagination)        |
| POST   | `/artists`               | Create a new artist                           |
| GET    | `/albums`                | List all albums                               |
| POST   | `/albums`                | Create a new album                            |
| GET    | `/tracks`                | List all tracks (searchable & paginated)      |
| POST   | `/tracks`                | Create a new track                            |
| GET    | `/tracks/<id>`           | Get detailed info for a specific track        |
| GET    | `/playlists`             | List all playlists                            |
| POST   | `/playlists`             | Create a new playlist                         |
| POST   | `/playlists/<id>/tracks` | Add tracks to a playlist                      |


## 🤝 Contributors

**Prince Patel** 

---

## 🛡️ License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this software, provided proper credit is given.  

