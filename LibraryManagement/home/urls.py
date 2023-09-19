from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), # to render homepage
    path('book', views.bookView, name='bookView'), # to render list of book page
    path('add_book_view', views.add_book_view, name='add_book_view'), #to render add book details form page
    path('add_book', views.add_book, name='add_book'), #to render add book details form page
    path('edit_book', views.edit_book_view, name='edit_book_view'), #to render edit book form page
    path('edit_book/update', views.update_book, name='update_book'), #to update book details
    path('delete_book', views.delete_book, name='delete_book'),

    path('members', views.membersView, name='membersView'),
    path('add_members_view', views.add_members_view, name='add_members_view'),  # to render add book details form page
    path('add_members', views.add_members, name='add_members'),
    path('edit_members', views.edit_members_view, name='edit_members_view'),
    path('edit_members/update', views.edit_members, name='edit_members'),
    path('delete_members', views.delete_members, name='delete_members'),

    path('transactions', views.transactionView, name='transactionView'),
    path('issue_book_view', views.issue_book_view, name='issue_book_view'),
    path('issue_book', views.issue_book, name='issue_book'),
    path('return_book', views.return_book_view, name='return_book_view'),
    path('return_book/update', views.return_book, name='return_book'),

    path('search_book', views.search_book, name='search_book'),
    path('import_data', views.import_data, name='import_data'),
]
