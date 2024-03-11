from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from .forms import BookForm, CategoryForm


# Create your views here.
def index(request):
    if request.method == "POST":
        addBook = BookForm(request.POST, request.FILES)
        if addBook.is_valid():
            addBook.save()
        addCategory = CategoryForm(request.POST)
        if addCategory.is_valid():
            addCategory.save()
    books = Book.objects.all()
    categories = Category.objects.all()
    form = BookForm()
    allbooks = Book.objects.filter(active=True).count()
    booksold = Book.objects.filter(status="sold").count()
    bookrental = Book.objects.filter(status="rental").count()
    bookavaible = Book.objects.filter(status="avaible").count()
    context = {
        "categories": categories,
        "books": books,
        "form": form,
        "catform": CategoryForm(),
        "allbooks": allbooks,
        "booksold": booksold,
        "bookrental": bookrental,
        "bookavaible": bookavaible,
    }
    return render(request, "pages/index.html", context)


def books(request):
    title = None
    search = Book.objects.all()

    if "search_name" in request.GET:
        title = request.GET["search_name"]

    if title:
        search = search.filter(title__icontains=title)

    if request.method == "POST":
        addCategory = CategoryForm(request.POST)
        if addCategory.is_valid():
            addCategory.save()

    books = Book.objects.all()
    categories = Category.objects.all()

    context = {
        "categories": categories,
        "books": search,
        "catform": CategoryForm(),
    }

    return render(request, "pages/books.html", context)


def update(request, id):
    book_instance = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES, instance=book_instance)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm(instance=book_instance)
    books = Book.objects.all()
    context = {
        "books": books,
        "form": book_form,
    }

    return render(request, "pages/update.html", context)


def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_delete.delete()
        return redirect("/")
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "books": books,
    }
    return render(request, "pages/delete.html", context)
