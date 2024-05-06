from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CompanyUser

class CompanyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CompanyUser
        fields = ['username', 'email', 'company_name', 'tin', 'user_name', 'tel']

class CompanyUserChangeForm(UserChangeForm):
    password = None
    
    class Meta(UserChangeForm.Meta):
        model = CompanyUser
        fields = ['email', 'user_name', 'tel']

    