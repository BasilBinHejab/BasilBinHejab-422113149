# Library Project - Lab 6 & Lab 7 Completion

This repository contains the completed tasks for Lab 6 (Django Forms) and Lab 7 (Django Models Part 1).

## Tasks Completed:

### Lab 6: Django Forms
- **Build HTML form template**: Created search.html using the master template base.html, including Font Awesome and custom CSS.
- **View function and URL**: Added search view in views.py and registered /books/search/.
- **Form Handling**: Implemented logic to handle POST data, filtering a static book list based on keywords and checkboxes.
- **Results Display**: Created bookList.html to list filtered books.

### Lab 7: Django Models (Part 1)
- **Database Schema**: Defined the Book model in models.py with title, author, price, and edition.
- **Migrations**: Ran makemigrations and migrate to create the database table.
- **Data Entry**: Inserted the specified initial books and additional mock data from Mockaroo.
- **Simple Queries**: Added simple_query view to filter books containing 'and' in the title.
- **Complex Queries**: Added complex_query view using advanced lookup conditions like isnull, icontains, gte, and exclude.
- **Result Links**:
    - **Simple Query**: http://127.0.0.1:8000/books/simple/query
    - **Complex Query**: http://127.0.0.1:8000/books/complex/query

## Running the Server:
To view the application, run:
```bash
python manage.py runserver
```
Then navigate to the links above.
