from django.urls import path 
from . import views
from .api_views import BookList, ToggleReadStatus, BookDetail, CategoryView, UserCreate
from rest_framework.authtoken.views import obtain_auth_token

 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('books/toggle/<int:book_id>', views.toggle_read_status, name='toggle_read_status'),
    path('books/edit/<int:book_id>', views.edit_book, name='edit_book'),
    path('api/books', BookList.as_view()),
    path('api/books/<int:pk>', BookDetail.as_view()),
    path('api/books/<int:pk>', ToggleReadStatus.as_view()),
    path('api/categories', CategoryView.as_view()),
    path('api/categories/<int:pk>', CategoryView.as_view()),
    path('api/users/create', UserCreate.as_view()),
    path('api/users/login', obtain_auth_token, name='api_token_auth')
]