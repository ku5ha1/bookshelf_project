# 📚 BookShelf – Django + DRF Project

A minimal library tracker app built with **Django**, using **Tailwind CSS** for templates and **Django REST Framework** for APIs.

---

## 🚀 Features

- Add, view, edit, and mark books as read/unread
- Categorize books
- User authentication via token-based login
- Clean API endpoints with DRF
- Responsive templates styled with Tailwind CSS

---

## 📁 Routes Overview

### 🖥 Web Views
- `/home/` – Homepage
- `/books/` – Book list
- `/books/add/` – Add new book
- `/books/<id>` – Book detail
- `/books/edit/<id>` – Edit book
- `/books/toggle/<id>` – Toggle read status

### 🔌 API Endpoints
- `/api/books` – List & create books
- `/api/books/<id>` – Retrieve, update, delete
- `/api/categories` – List & create categories
- `/api/users/create` – Register user
- `/api/users/login` – Token login

---

## ⚙️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Django templates + Tailwind CSS
- **Auth**: Token-based (DRF)

---

## ✅ Getting Started

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
