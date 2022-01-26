from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('user/<username>/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('books/', views.books_view, name='books'),
    path('loan_book/', views.loan_book, name='loan_book'),
]