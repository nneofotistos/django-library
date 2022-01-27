from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    isbn = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title) + " ["+str(self.isbn)+']'
    
class UserClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user)
    
def expiry():
    return datetime.today() + timedelta(days=14)
class LoanedBook(models.Model):
    user_id = models.CharField(max_length=100, blank=True)
    isbn = models.CharField(max_length=13)
    loan_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

    def __str__(self):
        return str(self.user_id ) + " ["+str(self.isbn)+']' + " ["+str(self.expiry_date)+']' 
