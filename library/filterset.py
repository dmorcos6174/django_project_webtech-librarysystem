import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')

    publication_year = django_filters.DateTimeFilter(field_name='date_posted', lookup_expr='year')
  ##  publication_year__gt = django_filters.NumberFilter(field_name='publication_year', lookup_expr='year__gt')
  ## publication_year__lt = django_filters.NumberFilter(field_name='publication_year', lookup_expr='year__lt')

    author__name = django_filters.CharFilter(field_name='author',lookup_expr='icontains')
    isbn = django_filters.CharFilter(field_name='isbn',lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ['book_author','title', 'isbn', 'date_posted']