# Lab 3: Django and MVT Architecture

This repository contains the solution for Lab 3.

## Output URLs (Localhost)
To test the functionality, run the server using `python manage.py runserver` and visit the following URLs:

1. **Main Index Page:** [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)
2. **GET Parameter Test:** [http://127.0.0.1:8000/books/?name=Basil](http://127.0.0.1:8000/books/?name=Basil)
3. **URL Path Parameter Test:** [http://127.0.0.1:8000/books/index2/123/](http://127.0.0.1:8000/books/index2/123/)
4. **Book Details (Task 7):** [http://127.0.0.1:8000/books/123](http://127.0.0.1:8000/books/123)

## Task Implementation Details
- **Task 1-3:** Basic views and URL mapping with parameters.
- **Task 4-5:** Template setup and rendering with context.
- **Task 6:** Modularized URL configuration using `include()`.
- **Task 7:** Dynamic book details viewing.
