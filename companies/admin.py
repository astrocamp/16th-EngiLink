from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CompanyUserCreationForm, CompanyUserChangeForm
from .models import CompanyUser

class CompanyUserAdmin(UserAdmin):
    add_form = CompanyUserCreationForm
    form = CompanyUserChangeForm
    model = CompanyUser
    list_display = ['username', 'email', 'company_name', 'tin', 'user_name', 'tel']

admin.site.register(CompanyUser, CompanyUserAdmin)
