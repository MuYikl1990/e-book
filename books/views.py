from django.shortcuts import render
from .models import Books
from .enums import *
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    python_new = Books.objects.get_books_by_type(PYTHON, limit=3, sort='new')
    python_hot = Books.objects.get_books_by_type(PYTHON, limit=4, sort='hot')
    javascript_new = Books.objects.get_books_by_type(JAVASCRIPT, limit=3, sort='new')
    javascript_hot = Books.objects.get_books_by_type(JAVASCRIPT, limit=4, sort='hot')
    algorithms_new = Books.objects.get_books_by_type(ALGORITHMS, limit=3, sort='new')
    algorithms_hot = Books.objects.get_books_by_type(ALGORITHMS, limit=4, sort='hot')
    machinelearning_new = Books.objects.get_books_by_type(MACHINELEARNING, limit=3, sort='new')
    machinelearning_hot = Books.objects.get_books_by_type(MACHINELEARNING, limit=4, sort='hot')
    operationsystem_new = Books.objects.get_books_by_type(OPERATIONSYSTEM, limit=3, sort='new')
    operationsystem_hot = Books.objects.get_books_by_type(OPERATIONSYSTEM, limit=4, sort='hot')
    database_new = Books.objects.get_books_by_type(DATABASE, limit=3, sort='new')
    database_hot = Books.objects.get_books_by_type(DATABASE, limit=4, sort='hot')

    context = {
        'python_new': python_new,
        'python_hot': python_hot,
        'javascript_new': javascript_new,
        'javascript_hot': javascript_hot,
        'algorithms_new': algorithms_new,
        'algorithms_hot ': algorithms_hot ,
        'machinelearning_new': machinelearning_new,
        'machinelearning_hot': machinelearning_hot,
        'operationsystem_new': operationsystem_new,
        'operationsystem_hot': operationsystem_hot,
        'database_new': database_new,
        'database_hot': database_hot,
    }

    return render(request, 'books/index.html', context)

@login_required
def detail(request, books_id):
    books = Books.objects.get_books_by_id(books_id=books_id)

    if books is None:
        return HttpResponseRedirect(reverse('books:index'))

    books_list = Books.objects.get_books_by_type(type_id=books.type_id, limit=2, sort='new')
    type_title = BOOKS_TYPE[books.type_id]

    context = {'books': books, 'books_list': books_list, 'type_title': type_title}
    return render(request, 'books/detail.html', context)

@login_required
def list(request, type_id, page):
    sort = request.GET.get('sort', 'default')

    if type_id not in BOOKS_TYPE.keys():
        return HttpResponseRedirect(reverse('books:index'))

    books_list = Books.objects.get_books_by_type(type_id=type_id, sort=sort)

    paginator = Paginator(books_list, 1)
    num_pages = paginator.num_pages

    if page == '' or int(page) > num_pages:
        page = 1
    else:
        page = int(page)

    books_list = paginator.page(page)

    if num_pages < 5:
        pages = range(1, num_pages+1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        pages = range(num_pages-4, num_pages+1)
    else:
        pages = range(page-2, page+3)

    books_new = Books.objects.get_books_by_type(type_id=type_id, limit=2, sort='new')

    type_title = BOOKS_TYPE[int(type_id)]

    context = {'books_list': books_list, 'books_new': books_new, 'type_id': type_id, 'sort': sort, 'type_title': type_title, 'pages': pages}
    return render(request, 'books/list.html', context)