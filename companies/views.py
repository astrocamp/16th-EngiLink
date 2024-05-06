from .forms import CompanyUserCreationForm, CompanyUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CompanyUser

class IndexView(TemplateView):
    template_name = "companies/index.html"

class SignUpView(CreateView):
    form_class = CompanyUserCreationForm
    model = CompanyUser
    template_name = "companies/signup.html"
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyUser
    form_class = CompanyUserChangeForm
    template_name = "companies/edit.html"
    success_url = reverse_lazy("index")
    
    def get_object(self):
        return self.request.user

class ProfileView(LoginRequiredMixin, DetailView):
    model = CompanyUser
    form_class = CompanyUserChangeForm
    template_name = 'companies/profile.html'
    context_object_name = 'user'