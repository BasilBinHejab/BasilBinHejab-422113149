from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Address, Student
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min

def index(request):
    return render(request, 'bookmodule/index.html')

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
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

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
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
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
