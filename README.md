# Inventory Management API

A production-ready backend REST API for managing inventory, suppliers, and stock movements.

Built using:

* Django
* Django REST Framework
* PostgreSQL

This API allows authenticated users to manage inventory items, track stock changes, and maintain supplier relationships in a secure and scalable way.

---

# 📌 Overview

The Inventory Management API is designed to simulate a real-world inventory system used in retail or warehouse environments.

The system supports:

* Supplier management
* Product management
* Stock tracking (stock-in and stock-out)
* Ownership-based access control
* Audit logging of inventory changes
* Secure authentication

The architecture follows clean backend layering and relational database best practices.

---

# 🏗 Architecture

The project is modular and divided into domain-specific Django apps:

```
inventory_api/
│
├── users/
├── suppliers/
├── products/
├── stock/
```

Each app handles a specific responsibility:

* users → authentication logic
* suppliers → supplier data management
* products → inventory items
* stock → stock movement history and auditing

This modular structure ensures maintainability and scalability.

---

# 🗄 Database Design

The system uses PostgreSQL as its database backend.

## Core Models

### Supplier

Represents companies or individuals that provide inventory items.

Fields:

* id
* name
* contact_email
* phone_number
* created_at

---

### Product

Represents inventory items stored in the system.

Fields:

* id
* name
* description
* category
* quantity_in_stock
* price
* owner (ForeignKey to User)
* supplier (ForeignKey to Supplier)
* created_at
* updated_at

Design considerations:

* quantity_in_stock is restricted to non-negative values
* price uses DecimalField for financial precision
* ownership ensures users can only manage their own products
* supplier relationship is optional

---

### StockMovement

Tracks inventory changes for audit purposes.

Fields:

* id
* product (ForeignKey to Product)
* movement_type (IN / OUT)
* quantity
* performed_by (ForeignKey to User)
* timestamp

Design considerations:

* movement_type is restricted to controlled values
* stock changes are traceable by user and time
* historical tracking supports reporting and auditing

---

# 🔐 Authentication & Security

Authentication is required for all API endpoints.

The API uses:

* SessionAuthentication
* TokenAuthentication

Default permission:

```
IsAuthenticated
```

This ensures that no inventory operations can be performed without valid authentication credentials.

Ownership enforcement ensures users can only modify products they own.

---

# 🌐 API Endpoints (Implemented So Far)

## Suppliers

Base route:

```
/api/suppliers/
```

Supported operations:

* GET → List suppliers
* POST → Create supplier
* GET /{id}/ → Retrieve supplier
* PUT /{id}/ → Update supplier
* PATCH /{id}/ → Partial update
* DELETE /{id}/ → Delete supplier

All endpoints require authentication.

---

# 📦 Installation & Setup

## 1. Clone the Repository

```
git clone https://github.com/your-username/inventory-management-api.git
cd inventory-management-api
```

## 2. Create Virtual Environment

```
python -m venv env
.\env\Scripts\Activate
```

## 3. Install Dependencies

```
pip install django
pip install djangorestframework
pip install psycopg[binary]
```

## 4. Configure PostgreSQL

Create a PostgreSQL database:

```
inventory_db
```

Update `settings.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## 5. Apply Migrations

```
python manage.py migrate
```

## 6. Run Development Server

```
python manage.py runserver
```

Access:

```
http://127.0.0.1:8000/api/suppliers/
```

---

# 🧠 Design Principles Applied

* Separation of concerns (modular apps)
* Relational integrity through ForeignKey constraints
* Defensive modeling using PositiveIntegerField
* Financial precision using DecimalField
* Controlled domain values using choices
* Audit logging for traceability
* Security by default (global IsAuthenticated)
* Pagination enabled globally

---

# 📈 Planned Enhancements

* Product API endpoints
* Stock movement increase/decrease logic
* Ownership validation enforcement
* Filtering and sorting for products
* Low-stock alerts
* Authentication endpoints (register/login)
* Deployment configuration
* API documentation

---

# 🛠 Technologies Used

* Python
* Django
* Django REST Framework
* PostgreSQL
* Git

---


