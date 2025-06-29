from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books' : books})

# Create your views here.
