from .forms import CompanyUserCreationForm, CompanyUserChangeForm
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Company

class LogOutView(LogoutView):
    template_name = "companies/logout.html"
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "登出成功!")
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class LogInView(LoginView):
    template_name = "companies/login.html"

    def get_success_url(self):
        url = self.get_redirect_url()
        return reverse("index") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST' and not self.request.POST.get('user_name') and not self.request.POST.get('password'):
            messages.info(self.request, "請輸入使用者代號與密碼!")
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "登入成功!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "登入失敗, 請確認輸入的訊息!")
        return self.render_to_response(self.get_context_data(form=form))
class IndexView(TemplateView):
    template_name = "companies/index.html"

class SignUpView(CreateView):
    form_class = CompanyUserCreationForm
    model = Company
    template_name = "companies/signup.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "註冊成功!")
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response
    

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyUserChangeForm
    template_name = "companies/edit.html"
    success_url = reverse_lazy("index")
    
    def get_object(self):
        return self.request.user

class ProfileView(LoginRequiredMixin, DetailView):
    model = Company
    form_class = CompanyUserChangeForm
    template_name = 'companies/profile.html'
    context_object_name = 'user'