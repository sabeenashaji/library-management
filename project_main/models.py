# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images/')
    num_copies = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

