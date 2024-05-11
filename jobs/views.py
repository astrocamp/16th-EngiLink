from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Job
from .forms import JobForm


class IndexView(ListView):
    template_name = "jobs/index.html"
    model = Job
    context_object_name = "jobs"


class AddView(CreateView):
    template_name = "jobs/create.html"
    model = Job
    form_class = JobForm
    success_url = reverse_lazy("jobs:index")

    def form_valid(self, form):
        messages.success(self.request, "新增成功!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "新增失敗, 請確認輸入的欄位!")
        return self.render_to_response(self.get_context_data(form=form))

class ShowView(DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/show.html"


class EditView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = "jobs/edit.html"
    context_object_name = "job"
    success_url = reverse_lazy("jobs:index")

    def form_valid(self, form):
        messages.success(self.request, "修改成功!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "修改失敗, 請確認輸入的欄位!")
        return self.render_to_response(self.get_context_data(form=form))

class JobDeleteView(DeleteView):
    model = Job

    def get_success_url(self):
        messages.success(self.request,"刪除成功")
        return reverse("jobs:index")