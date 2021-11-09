from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    book_author = models.CharField(max_length=100, default='Unknown') #####ACTUAL BOOK AUTHOR
    title = models.CharField(max_length=100)
    content = models.TextField()
    isbn = models.CharField(max_length=5, unique=True)
    borrowed = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #####ADMIN ONLY
    username = models.CharField(max_length=100, null=True)
    borrow_time = models.DateField(null=True)
    return_time = models.DateField(null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})