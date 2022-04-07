from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Book, LoanedBook, UserClass

class EmployeeInline(admin.StackedInline):
    model = UserClass
    can_delete = False
    verbose_name_plural = 'userclass'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(LoanedBook)

# Register your models here.
