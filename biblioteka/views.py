from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'biblioteka/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'biblioteka/book_detail.html', {'book': book})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'biblioteka/book_form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'biblioteka/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


def book_list(request):
    genre_filter = request.GET.get('genre')
    if genre_filter:
        books = Book.objects.filter(genre=genre_filter)
    else:
        books = Book.objects.all()
    genres = Book.GENRE_CHOICES
    return render(request, 'biblioteka/book_list.html', {
        'books': books,
        'genres': genres,
        'current_genre': genre_filter,
    })


def book_list(request):
    genre_filter = request.GET.get('genre')
    search_query = request.GET.get('q')

    books = Book.objects.all()

    if genre_filter:
        books = books.filter(genre=genre_filter)
    if search_query:
        books = books.filter(title__icontains=search_query)

    genres = Book.GENRE_CHOICES
    return render(request, 'biblioteka/book_list.html', {
        'books': books,
        'genres': genres,
        'current_genre': genre_filter,
        'search_query': search_query,
    })
