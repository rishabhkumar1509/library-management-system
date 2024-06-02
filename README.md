# FastAPI Library Management System

This project is a simple Library Management System API built with FastAPI, SQLAlchemy, and Pydantic. The application allows you to manage books, students, inventory, and book issuance.

## Features

- Add new books
- Register new students
- Update books inventory
- Issue books to students and return them
- Enforce a limit of 3 books per student at a time
- Proper error handling with HTTP 400 responses for various exceptions

## Project Structure


### `main.py`
Contains the FastAPI application and endpoint definitions.

### `database.py`
Configures the database connection using SQLAlchemy.

### `models.py`
Defines SQLAlchemy models for the tables.

### `schemas.py`
Defines Pydantic schemas for data validation.

### `crud.py`
Contains the CRUD operations for interacting with the database.

### `pyproject.toml`
Defines the dependencies required for the project.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/rishabhkumar1509/library-management-system.git
    cd library-management-system
    ```

2. **Install Poetry (if not already installed):**
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    After installation, make sure Poetry's bin directory is in your `PATH`. You can do this by adding `export PATH="$HOME/.local/bin:$PATH"` to your shell configuration file (e.g., `.bashrc`, `.zshrc`).

3. **Install the dependencies and create the virtual environment:**
    ```sh
    poetry install
    ```

4. **Activate the virtual environment:**
    ```sh
    poetry shell
    ```

5. **Set up the database:**
    Update the `DATABASE_URL` in `database.py` with your MySQL database connection string.
    ```python
    DATABASE_URL = "mysql://user:password@localhost/dbname"
    ```

6. **Create the database tables:**
    ```sh
    python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
    ```

7. **Run the application:**
    ```sh
    uvicorn main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Create a Student
- **URL:** `/students/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```

### Create a Book
- **URL:** `/books/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }
    ```

### Update Inventory
- **URL:** `/inventory/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "bookid": 1,
        "quantity": 5
    }
    ```
- **Response:**
    ```json
    {
        "bookid": 1,
        "quantity": 5
    }
    ```

### Issue a Book
- **URL:** `/issue/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "bookid": 1,
        "studentid": 1,
        "issue_date": "2023-01-01T00:00:00"
    }
    ```
- **Response:**
    ```json
    {
        "issueid": 1,
        "bookid": 1,
        "studentid": 1,
        "issue_date": "2023-01-01T00:00:00"
    }
    ```

### Return a Book
- **URL:** `/return/{issueid}`
- **Method:** `POST`
- **Response:**
    ```json
    {
        "issueid": 1,
        "bookid": 1,
        "studentid": 1,
        "issue_date": "2023-01-01T00:00:00"
    }
    ```

## Error Handling

- HTTP 400 errors are returned in cases such as:
  - Requesting a book that is not available in the library.
  - Requesting a book when the inventory is 0.
  - Issuing more than 3 books to a student.

