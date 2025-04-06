from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('bookstore-choice/', views.bookstore_choice_view, name='bookstore_choice'),
    path('buy-books/', views.buy_books_view, name='buy_books'),
    path('sell-books/', views.sell_books_view, name='sell_books'),
]