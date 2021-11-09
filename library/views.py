from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.


def home(request): #HOME PAGE
    userNum = User.objects.count()
    booksNum = Book.objects.count()
    return render(request, 'library/home.html', {
        'user_count' : userNum,
        'books_count' : booksNum,
    })

class BookListView(ListView): #BROWSE BOOKS
    model = Book
    template_name = 'library/browse_books.html'    #default naming: <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 5

class SearchResultsView(ListView):
    model = Book
    template_name = 'library/search_results.html'

    def get_queryset(self): # new
        if  self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            object_list = Book.objects.filter(
                Q(title__contains=query) | Q(isbn__exact=query)
            )
            return object_list

class UserBookListView(ListView):
    model = Book
    template_name = 'library/user_posts.html'
    context_object_name = 'book'
    ordering = ['-date_posted']
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(author=user).order_by('-date_posted')



class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'    #default naming: <app>/<model>_<viewtype>.html



class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['book_author','title', 'content', 'isbn', 'borrowed']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['book_author','title', 'content', 'isbn', 'borrowed']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BookBorrowView(UpdateView):
    model = Book
    fields = ['username']

    def form_valid(self, form):
        form.instance.borrowed = True
        form.instance.borrow_time = timezone.now()
        form.instance.return_time = timezone.now() + timezone.timedelta(days = 7)

        return super().form_valid(form)

class BookExtendPer(UpdateView):
    model = Book
    fields = ['return_time']

    def form_valid(self, form):
        return super().form_valid(form)



class BookReturnView(UpdateView):
    model = Book
    fields = ['borrowed']

    def form_valid(self, form):

        return super().form_valid(form)


def about(request):
    return render(request, 'library/about.html', {'title': 'About'})
    #return HttpResponse('<h1>Blog About</h1>')