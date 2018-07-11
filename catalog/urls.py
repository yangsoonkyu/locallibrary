
from django.conf.urls import url
from . import views




urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url('^$', views.index, name='index'),
    url('^books/$', views.BookListView.as_view(), name='books'),
    url('^books/(?P<pk>[0-9]+)/$', views.BookDetailView.as_view(), name='book_detail'),
    url('^authors/$', views.AuthorListView.as_view(), name='authors'),
    url('^author/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
]






