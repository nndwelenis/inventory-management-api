---

# Inventory Management API

A production-ready RESTful backend built with Django and Django REST Framework for managing products, suppliers, and stock movements for multiple shop owners.

Live API URL:

[https://inventory-management-api-e9qv.onrender.com/](https://inventory-management-api-e9qv.onrender.com/)

---

## Overview

This API allows authenticated users to:

* Register and log in using JWT authentication
* Manage their own products
* Track stock movements (IN and OUT)
* Prevent negative stock
* Filter low stock products
* View stock history

Each user can only access their own inventory data.

---

## Tech Stack

* Python 3
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication (SimpleJWT)
* Gunicorn
* Render (Deployment)

---

## Authentication

This API uses JWT (JSON Web Tokens).

### Register User

POST
/api/register/

Example body:

{
"username": "jay",
"email": "[jay@email.com](mailto:jay@email.com)",
"password": "strongpassword"
}

---

### Login

POST
/api/login/

Example body:

{
"username": "jay",
"password": "strongpassword"
}

Response:

{
"access": "your_access_token",
"refresh": "your_refresh_token"
}

Use the access token in all protected requests:

Authorization: Bearer your_access_token

---

## Core Endpoints

### Products

GET /api/products/
POST /api/products/

Supports:

* Low stock filter
  /api/products/?low_stock=true

* Ordering
  /api/products/?ordering=name

---

### Suppliers

GET /api/suppliers/
POST /api/suppliers/

---

### Stock Movements

POST /api/stock/

Movement types:

* IN (increase stock)
* OUT (decrease stock)

Business rules enforced:

* Stock cannot go negative
* Stock updates and movement logging are atomic
* Users cannot modify another user’s products

---

## Business Logic

### Ownership Security

All products and suppliers are tied to a specific user.

Users cannot:

* View other users’ products
* Modify other users’ stock
* Access foreign inventory data

---

### Stock Validation

When creating an OUT movement:

* The system checks available quantity
* If insufficient, request is rejected
* Transaction rollback ensures consistency

---

## Testing

Unit tests implemented for:

* Product ownership isolation
* Stock increase logic
* Prevention of negative stock
* Supplier creation

All tests pass successfully.

---

## Deployment

The project is deployed on Render using:

* Gunicorn production server
* PostgreSQL managed database
* Environment variable configuration
* Automatic migrations on startup

Production settings include:

* DEBUG disabled
* Environment-based configuration
* Secure SECRET_KEY handling
* Proper ALLOWED_HOSTS configuration

---

## Environment Variables

The following variables are required in production:

SECRET_KEY
DEBUG
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
ALLOWED_HOSTS

---

## How to Run Locally

1. Clone repository
2. Create virtual environment
3. Install dependencies

pip install -r requirements.txt

4. Configure .env file
5. Run migrations

python manage.py migrate

6. Start server

python manage.py runserver

---

## Project Status

Backend implementation complete.
Fully deployed and production-ready.

---

Now commit this:

git add README.md
git commit -m "Finalize professional project README with live deployment details"
git push

---

After that, tell me and we move to full production testing flow.
