from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='책에 대해 간단하게 설명하세요')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text='이 책의 장르를 선택하세요 ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book_detail', args=[str(self.id)])

    def display_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()[:3] ])

    display_genre.short_description = 'Genre'



class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="책의 고유 ID")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', '유지보수'),
        ('o', '대여중'),
        ('a', '대여가능'),
        ('r', '예약가능'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m', help_text='책의 상태')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '{0} ({1})'. format(self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField( null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse('catalog:author_detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1}'.format(self.last_name, self.first_name)

class Launguage(models.Model):
    name = models.CharField(max_length=200, help_text='책의 언어를 입력하십시오')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='책의 장르를 입력하세요 ')

    def __str__(self):
        return self.name
