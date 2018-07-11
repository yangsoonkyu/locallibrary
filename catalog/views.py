from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre



# Create your views here.

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    ten_list = Book.objects.filter(title__contains='십이').count()
    num_genre =Genre.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'catalog/index.html',
                  context={'num_books': num_books, 'num_instances': num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
                           'ten_list': ten_list, 'num_genre': num_genre, 'num_visits': num_visits})


# def BookListView(request):
#     book_list = Book.objects.all()
#     return render(request, 'catalog/book_list', {'book_list': book_list})

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'book_list'


    # 이부분 모르겠음
    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'author_list'

class AuthorDetailView(generic.DetailView):
    model = Author

