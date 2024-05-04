from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.views.generic import TemplateView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class UserIndexView(TemplateView):
    template_name = "users/index.html"


class SignupView(CreateView):
    model = User
    template_name = "users/signup.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('userindex')
    
    def form_valid(self, form):
        name = form.cleaned_data.get("username")
        messages.success(self.request, f"註冊成功, {name} 你好! 請登入")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/edit.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("userindex")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "更新完成!")
        return super().form_valid(form)

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'