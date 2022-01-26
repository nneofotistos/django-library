from django import forms
from django.contrib.auth.models import User
from . import models

class LoanBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Book Title [ISBN]", to_field_name="isbn", label="Book (Title and ISBN)")
    name2 = forms.ModelChoiceField(queryset=models.User.objects.all(), empty_label="Name", to_field_name="username", label="User Details")

    isbn2.widget.attrs.update({'class':'form-control'})
    name2.widget.attrs.update({'class':'form-control'})