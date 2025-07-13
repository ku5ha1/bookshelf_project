from django.urls import path 
from . import views
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('books/toggle/<int:book_id>', views.toggle_read_status, name='toggle_read_status'),
    path('books/edit/<int:book_id>', views.edit_book, name='edit_book')
]