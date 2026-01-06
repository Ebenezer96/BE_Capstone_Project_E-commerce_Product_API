E-commerce Product API
Project Overview

This project is a backend REST API built with Django and Django REST Framework for managing products in an e-commerce platform.
It allows authenticated users to create, update, delete, and view products, while providing public access to browse products and categories. The API also supports search, filtering, pagination, and secure authentication using JWT.

Features

User authentication using JWT (access & refresh tokens)

Admin-only user management (CRUD)

Product management (CRUD)

Category management

Product search by name and category (partial matching)

Filtering by category, price range, and stock availability

Pagination for large datasets

Secure, RESTful API design

Tech Stack

Python

Django

Django REST Framework

Django Filters

Simple JWT

SQLite (development database)

Project Structure
BE_Capstone_Project/
├── config/
├── products/
├── users/
├── manage.py
└── requirements.txt

Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd BE_Capstone_Project

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Create a superuser
python manage.py createsuperuser

6. Start the development server
python manage.py runserver

Authentication (JWT)
Obtain token
POST /api/token/


Request body:

{
  "username": "your_username",
  "password": "your_password"
}

Refresh token
POST /api/token/refresh/

API Endpoints
Products
Method	Endpoint	Description
GET	/api/products/	List products (paginated)
POST	/api/products/	Create product (auth required)
GET	/api/products/{id}/	Retrieve product
PUT	/api/products/{id}/	Update product (auth required)
DELETE	/api/products/{id}/	Delete product (auth required)
Categories
Method	Endpoint	Description
GET	/api/categories/	List categories
POST	/api/categories/	Create category (auth required)
Users (Admin Only)
Method	Endpoint	Description
GET	/api/users/	List users
POST	/api/users/	Create user
GET	/api/users/{id}/	Retrieve user
PUT	/api/users/{id}/	Update user
DELETE	/api/users/{id}/	Delete user
Search, Filtering & Pagination

Search products by name or category:

/api/products/?search=laptop


Filter by category:

/api/products/?category=1


Pagination:

/api/products/?page=2

Permissions & Access Control

Public users can view products and categories

Authenticated users can create, update, and delete products

User management endpoints are restricted to admin users only

Passwords are securely hashed and never exposed via the API