# SQLAlchemy E-Commerce Database Assignment

This project demonstrates how to build and interact with a relational database using SQLAlchemy ORM in Python. It models a simple e-commerce system with users, products, and orders, including many-to-many relationships.

---

## 📌 Features

- Define database models using SQLAlchemy ORM:
  - User
  - Product
  - Order
- Implement many-to-many relationships:
  - Users ↔ Orders
  - Products ↔ Orders
- Perform common database operations:
  - Retrieve users, products, and orders
  - Update product prices
  - Filter orders by status
  - Count total orders per user
- Use modern SQLAlchemy 2.0 querying (`select()` + `scalars()`)

---

## 🧠 Database Structure

### Tables:
- **users**
- **products**
- **orders**
- **user_orders** (association table)
- **product_orders** (association table)

### Relationships:
- A user can have multiple orders
- An order can belong to multiple users
- An order can contain multiple products

---

## ⚙️ Technologies Used

- Python 3
- SQLAlchemy ORM
- MySQL
- mysql-connector

---

## 🚀 Setup Instructions

### 1. Install dependencies

```bash
pip install sqlalchemy mysql-connector-python
