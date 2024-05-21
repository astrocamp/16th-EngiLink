from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .forms import CompanyRegisterForm, CompanyUpdateForm
from users.models import CustomUser
from .models import Company

class CompanyRegisterView(FormView):
    template_name = 'companies/register.html'
    form_class = CompanyRegisterForm


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(CompanyRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        user = self.request.user
        company = Company.objects.filter(custom_user=user).first()

        if user.user_type == 2 and company is None:
            print("Redirecting to companies:update")
            return reverse_lazy('companies:update',kwargs={'pk': user.pk})
        else:
            return reverse_lazy('companies:home')

class CompanyHomeView(TemplateView):
    template_name = 'companies/home.html'

class CompanyLoginView(LoginView):
    template_name = 'companies/login.html'

    def get_success_url(self):
        return reverse_lazy('companies:home')

class CompanyLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'companies/detail.html'
    context_object_name = 'user'
    login_url = "/companies/"

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=2)

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CompanyUpdateForm
    template_name = 'companies/update.html'
    success_url = "/companies/"
    login_url = "/companies/"

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=2, id=self.request.user.id)
    

class CompanyPasswordChangeView(PasswordChangeView):
    template_name="companies/password_change_form.html"
    success_url="/companies/"

    def form_valid(self, form):
        response = super().form_valid(form)
        logout(self.request)
        return response
    
def CompanyListView(request):
    companies = Company.objects.all()
    paginator = Paginator(companies, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'companies/list.html', {'page_obj': page_obj})