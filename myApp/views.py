from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
# Create your views here.
def test_book (request):
    return HttpResponse ('<h1> Tutaj będą książki </h1>')


class Second(View):

    def get (self, request):

        books = Book.objects.all()

        lenBook = f"W bazie mamy {len(books)} książki:"

        titleBook = ""

        for oneBook in books:
            titleBook += f"Tytuły książek: {oneBook.title} <br>"
        
        # Tylko przeczytane książki
        readOnly = Book.objects.filter(read_book="Tak")
        
        read_books = [read.title for read in readOnly]
        read_books_tekst = f"Przeczytane książki: {' , '.join(read_books)}"

        # Wybór tylko jednej książki z id = 1
        id_book_one = Book.objects.get(id=1)
        
        content = f"{lenBook} <br> {titleBook} <br> {read_books_tekst} <br> {id_book_one}"

        return HttpResponse (content)
        
def testTempate (request):
    return render (request, 'myApp.html')


def testDynamic (request):
    allBook = Book.objects.all()
    return render(request, 'dynamic.html', {'book': allBook})