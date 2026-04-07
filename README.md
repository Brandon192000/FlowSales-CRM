# 🚀 FlowSales CRM - Automation Platform

![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![Architecture](https://img.shields.io/badge/Architecture-Clean-blueviolet)

FlowSales is a scalable CRM and automation platform designed to help businesses manage leads, streamline sales processes, and eliminate repetitive tasks.

This project is built using **Clean Architecture principles**, ensuring high maintainability, scalability, and separation of concerns.

---

## 🧠 Overview

FlowSales aims to provide a modern backend system that:

- Manages leads efficiently  
- Automates repetitive business processes  
- Improves sales tracking and performance  
- Serves as a foundation for a SaaS platform  

This is not just a CRUD system — it is designed with **real-world business use cases in mind**.

---

## 🏗️ Architecture

The project follows a **Clean Architecture approach**, separating responsibilities into layers:

apps/  
└── leads/  
  ├── domain/ → Business logic (pure Python)  
  ├── application/ → Use cases & services  
  ├── infrastructure/ → ORM & database layer  
  └── presentation/ → API layer (Django REST Framework)  

### Key Principles:

- SOLID principles  
- Single Responsibility Principle (SRP)  
- Separation of Concerns  
- Decoupled architecture  
- Scalable modular design  

---

## ⚙️ Tech Stack

### Backend
- Python 3.11+  
- Django 5+  
- Django REST Framework  

### Database
- PostgreSQL  

### Tools
- Git & GitHub  
- VS Code  
- Virtual Environments (venv)  

---

## 📦 Features

### ✅ Current Features
- Clean architecture structure  
- Lead model with best practices  
- PostgreSQL integration  
- Modular and scalable project setup  

### 🚧 In Progress
- Lead CRUD API (DRF)  
- Filtering and search  
- Lead assignment system  
- API structure following best practices  

### 🔮 Planned Features
- Sales pipeline management  
- Task and activity tracking  
- Automation workflows  
- Email / WhatsApp notifications  
- Role-based access control (RBAC)  
- Multi-tenant SaaS architecture  

---

## 🛠️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/your-username/flowsales.git  
cd flowsales  

---

### 2. Create virtual environment

python -m venv venv  
venv\Scripts\activate  

---

### 3. Install dependencies

pip install django djangorestframework psycopg2-binary  

---

### 4. Configure PostgreSQL

Create database:

CREATE DATABASE flowsales_db;

Then update:

config/settings.py

DATABASES = {  
  'default': {  
    'ENGINE': 'django.db.backends.postgresql',  
    'NAME': 'flowsales_db',  
    'USER': 'postgres',  
    'PASSWORD': 'your_password',  
    'HOST': 'localhost',  
    'PORT': '5432',  
  }  
}  

---

### 5. Run migrations

python manage.py makemigrations  
python manage.py migrate  

---

### 6. Create superuser

python manage.py createsuperuser  

---

### 7. Run server

python manage.py runserver  

Open in browser:

http://127.0.0.1:8000/admin/

---

## 📌 Project Structure

crm-automatization/  
├── config/  
│  ├── settings.py  
│  ├── urls.py  
│  
├── apps/  
│  └── leads/  
│    ├── domain/  
│    │  ├── entities.py  
│    │  ├── constants.py  
│    │  └── rules.py  
│    │  
│    ├── application/  
│    │  ├── use_cases.py  
│    │  ├── services.py  
│    │  └── dto.py  
│    │  
│    ├── infrastructure/  
│    │  ├── models.py  
│    │  ├── repositories.py  
│    │  └── mappers.py  
│    │  
│    ├── presentation/  
│    │  ├── serializers.py  
│    │  ├── views.py  
│    │  └── urls.py  
│    │  
│    ├── admin.py  
│    ├── apps.py  
│    ├── models.py  
│    └── views.py  

---

## 🧩 Design Decisions

- Django ORM isolated in infrastructure layer  
- Domain layer independent of Django  
- Business logic handled in application layer  
- API layer separated using DRF  
- Ready for SaaS scaling  

---

## 🧪 Future Improvements

- Swagger / OpenAPI documentation  
- Unit and integration tests  
- Docker support  
- CI/CD pipelines  
- Performance optimization  
- Redis caching  

---

## 👨‍💻 Author

Brandon Blanco Chinchilla  

- Full-Stack Developer  
- Backend-focused (Django, APIs, Clean Architecture)  
- Passionate about scalable systems and performance  

---

## ⭐ Final Notes

This project is actively being developed and improved.

It serves as:

- A real-world backend architecture reference  
- A scalable foundation for a SaaS CRM product  

Contributions, feedback, and ideas are welcome 🚀
