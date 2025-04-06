from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')

    return render(request, 'books/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('bookstore_choice')  
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'books/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def landing_page(request):
    return render(request, 'books/landing_page.html')


@login_required
def bookstore_choice_view(request):
    return render(request, 'books/bookstore_choice.html')


@login_required
def buy_books_view(request):
    books = [
        {'title': 'Software Engineering', 'author': 'Lan Sommerville', 'price': ' 500', 'condition': 'Good'},
        {'title': 'Calculus 101', 'author': 'Johnson', 'price': ' 650', 'condition': 'Excellent'},
        {'title': 'Introduction to Psychology', 'author': 'Brown', 'price': ' 300', 'condition': 'Fair'},
    ]
    return render(request, 'books/buy_books.html', {'books': books})



@login_required
def sell_books_view(request):
    if request.method == 'POST':
        messages.success(request, 'Book listed successfully .')
        return redirect('sell_books') 
    return render(request, 'books/sell_books.html')

def logout_view(request):
    logout(request)
    return redirect('landing_page')  

