# FastAPI Todo CRUD

A simple Todo application built using **FastAPI** while learning backend development and REST API fundamentals.

This project focuses on understanding how to create API endpoints, manage database sessions, connect to a database, and validate request data.

## 🛠️ Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## 📁 Project Structure

```text
FastAPI-Todo-CRUD/
│
├── app.py
├── todo.py
├── database.py
├── schema.py
└── README.md
```

## 📌 File Description

### 1. app.py
- Contains the POST API endpoint.
- Implements the Todo creation operation.
- Handles incoming requests to create new Todo records.

### 2. todo.py
- Contains the database session-related code.
- Handles session management for database operations.

### 3. database.py
- Handles database configuration.
- Establishes the database connection.
- Configures SQLAlchemy.

### 4. schema.py
- Defines Pydantic schemas.
- Validates incoming request data.
- Defines the structure of Todo data.

## 🔄 CRUD Operations

CRUD stands for:

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Create a new Todo |
| Read | GET | Retrieve Todo data |
| Update | PUT | Update existing Todo data |
| Delete | DELETE | Delete a Todo |

## 🎯 Learning Objectives

Through this project, I practiced:

- FastAPI fundamentals
- Creating REST API endpoints
- Database session management
- SQLAlchemy integration
- Pydantic data validation
- Backend application structure

## 👨‍💻 Author

Built as a hands-on practice project during my journey of learning Python and FastAPI.