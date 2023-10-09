from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def test_book (request):
    return HttpResponse ('<h1> Tutaj będą książki </h1>')


class Second(View):

    def get (self, request):
        return HttpResponse ('Książka - podstrona')
