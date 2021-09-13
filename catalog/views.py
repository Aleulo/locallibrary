from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # The dictionary of genres and the quantity of it
    genre_name_dict = {}
    #number of books with specific genre
    genre_list = list(Genre.objects.values_list('name', flat=True))

    # this function counts genres and returnt quantity
    def count_genres(genre):
         return Book.objects.filter(genre__name__icontains=genre).count()
    # assign the genre to quantity in dictionary
    for genre in genre_list:
        genre_name_dict[genre] = count_genres(genre)

     #this is formated dictionary to present on the website
    new_format = ""
    for key, value in genre_name_dict.items():
        new_format += "{}: {}, \n".format(key, value)



    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'genre': new_format,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
