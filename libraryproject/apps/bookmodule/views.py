from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return render(request, 'bookmodule/index.html')

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

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
    mybooks = Book.objects.filter(title__icontains='continuous').order_by('id')[:1]
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

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(edition__gte=2).exclude(price__lt=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def lookup_query(request):
    return complex_query(request)
