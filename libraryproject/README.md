# Library Project - Lab 6 & Lab 7 Completion

This repository contains the completed tasks for Lab 6 (Django Forms) and Lab 7 (Django Models Part 1).

## Tasks Completed:
### Lab 6: Django Forms
- **search.html**: Created a search form template with CSS styling and Font Awesome icons.
- **Form Handling**: Implemented logic in `views.py` to handle POST requests, filtering a static list of books based on keywords and selection (Title/Author).
- **URL Configuration**: Registered `/books/search/` route.

### Lab 7: Django Models (Part 1)
- **Database Schema**: Defined the `Book` model in `models.py` with fields: `title`, `author`, `price`, and `edition`.
- **Migrations**: Performed `makemigrations` and `migrate` to set up the SQLite database.
- **Data Seeding**: Populated the database with initial book records and additional mock data to simulate a real-world scenario (Mockaroo).
- **Queries & Links**:
    - **Simple Query**: [http://127.0.0.1:8000/books/simple/query](http://127.0.0.1:8000/books/simple/query) - Filters books containing "and" in the title.
    - **Complex Query**: [http://127.0.0.1:8000/books/complex/query](http://127.0.0.1:8000/books/complex/query) - Uses advanced filters (`isnull`, `gte`, `exclude`, and slicing).
- **Template Update**: Updated `bookList.html` to dynamically display model data (ID and Title).

## How to Run:
1. Ensure you have Django installed.
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Access the features at:
    - Search: `http://127.0.0.1:8000/books/search/`
    - Simple Query: `http://127.0.0.1:8000/books/simple/query`
    - Complex Query: `http://127.0.0.1:8000/books/complex/query`

---
**Note:** The database `db.sqlite3` is already migrated and contains the required data for testing.
