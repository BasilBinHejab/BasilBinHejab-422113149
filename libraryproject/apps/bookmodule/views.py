from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Address, Student, Publisher, Author
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min, F

def index(request):
    return render(request, 'bookmodule/index.html')

def lab9_task1(request):
    books = Book.objects.all()
    # Task 1: percentage availability. 
    # Example: If total books in 350 and quantity of a book is 7, then 7/350 * 100 = 2%
    # We will use 350 as the total stock for the calculation as per the example.
    total_stock = 350 
    for book in books:
        book.availability = (book.quantity / total_stock) * 100
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def lab9_task2(request):
    # Task 2: List books that all publishers, annotated with their respective total book stock.
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    # Task 3: Get oldest book of any of those managed by every publisher.
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    # Task 4: Calculate the average, min, and max price of books for each publisher.
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def lab9_task5(request):
    # Task 5: List publishers with a count of highly rated books (rating > 3).
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gt=3))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

def lab9_task6(request):
    # Task 6: Count of books for each publisher, filter only books with price > 50 and 1 <= quantity < 5.
    publishers = Publisher.objects.annotate(
        book_count=Count('book', filter=Q(book__price__gt=50, book__quantity__gte=1, book__quantity__lt=5))
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})


def list_books(request):
    mybooks = Book.objects.all().order_by('id')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def __getBooksList():
    book1 = {'id': 1, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley', 'price': 120.00, 'edition': 3}
    book2 = {'id': 2, 'title': 'Reversing: Secrets of Reverse Engineer', 'author': 'E. Eilam', 'price': 97.00, 'edition': 2}
    book3 = {'id': 3, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov', 'price': 100.00, 'edition': 4}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

def insert_books():
    Book.objects.create(title="Continuous Delivery", author="J.Humble and D. Farley", price=120.00, edition=3)
    Book.objects.create(title="Reversing: Secrets of Reverse Engineer", author="E. Eilam", price=97.00, edition=2)
    Book.objects.create(title="The Hundred-Page Machine Learning Book", author="Andriy Burkov", price=100.00, edition=4)

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task1(request):
    mybooks = Book.objects.filter(price__lte=80)
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task2(request):
    mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task3(request):
    mybooks = Book.objects.filter(~Q(edition__gt=3) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_stats.html', {'stats': stats})

def lab8_task7(request):
    # Get cities with the count of students in each
    # Addresses that have students
    city_counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'city_counts': city_counts})

# Lab 10 Views

from django.shortcuts import redirect

def lab10_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks.html', {'books': books})

def lab10_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        Book.objects.create(title=title, price=price, quantity=quantity, rating=rating)
        return redirect('books.lab10_listbooks')
    return render(request, 'bookmodule/lab10_addbook.html')

def lab10_editbook(request, bookId):
    book = Book.objects.get(id=bookId)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.rating = request.POST.get('rating')
        book.save()
        return redirect('books.lab10_listbooks')
    return render(request, 'bookmodule/lab10_editbook.html', {'book': book})

def lab10_deletebook(request, bookId):
    book = Book.objects.get(id=bookId)
    book.delete()
    return redirect('books.lab10_listbooks')

# Lab 10 Part 2 Views (Using Django Forms)

from .forms import BookForm

def lab10_listbooks_v2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks_v2.html', {'books': books})

def lab10_addbook_v2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.lab10_listbooks_v2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_addbook_v2.html', {'form': form})

def lab10_editbook_v2(request, bookId):
    book = Book.objects.get(id=bookId)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.lab10_listbooks_v2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_editbook_v2.html', {'form': form, 'book': book})

def lab10_deletebook_v2(request, bookId):
    book = Book.objects.get(id=bookId)
    book.delete()
    return redirect('books.lab10_listbooks_v2')
