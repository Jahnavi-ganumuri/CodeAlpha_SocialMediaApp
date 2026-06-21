# CodeAlpha Social Media App

## Project Description

A mini social media platform developed as part of the CodeAlpha Internship.

This application allows users to register, authenticate using JWT, create posts, add comments, like posts, follow other users, and search users.

---

## Features

- User registration
- JWT authentication
- User profiles
- Create, update, delete posts
- Comments system
- Like / Unlike posts
- Follow / Unfollow users
- Search users
- Pagination support
- Swagger API documentation

---

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Django
- Django REST Framework
- JWT Authentication

### Database
- SQLite

### API Documentation
- Swagger (drf-spectacular)

---
## Project Structure

```
codeaplha_socialmedial/
├── backend/
├── frontend/
├── .gitignore
├── README.md
```

---

## Installation and Setup

### 1. Clone Repository
git clone https://github.com/Jahnavi-ganumuri/CodeAlpha_SocialMediaApp.git
cd CodeAlpha_SocialMediaApp

### 2. Navigate to Backend Folder
cd backend

### 3. Create Virtual Environment
python -m venv env

### 4. Activate Virtual Environment

Windows:
env\Scripts\activate

Mac/Linux:
source env/bin/activate

### 5. Install Requirements
pip install -r requirements.txt

### 6. Run Migrations
python manage.py migrate

### 7. Start Server
python manage.py runserver

---

## API Documentation

If Swagger is enabled:
http://127.0.0.1:8000/api/docs/

---

## Features Implemented

- User registration & login (JWT)
- Post creation & management
- Comments system
- Like / Unlike functionality
- Follow system
- User search
- Profile handling

---

## Author

Jahnavi Ganumuri
CodeAlpha Internship Project
