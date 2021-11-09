from django.conf.urls import url
from django.urls import path
from . import views
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, UserBookListView,BookReturnView,BookBorrowView,BookExtendPer,SearchResultsView

urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('browse_books/', BookListView.as_view(), name='browse-books'),
    path('browse_books_search/', SearchResultsView.as_view(), name='browse-books-search'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/borrow/', BookBorrowView.as_view(), name='book-borrow'),
    path('book/<int:pk>/return/', BookReturnView.as_view(), name='book-return'),
    path('book/<int:pk>/extend/', BookExtendPer.as_view(), name='book-extend'),
    path('user/<str:username>', UserBookListView.as_view(), name='user-posts'),
]
