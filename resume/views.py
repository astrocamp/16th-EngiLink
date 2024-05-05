from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .forms import ProfileForm
from .models import Profile
from django.core.paginator import Paginator

# 履歷區（前往建立履歷）
class ResumeArea(TemplateView):
    template_name = 'resume_home/resume_area.html'

# 建立第一份履歷(基本資料/教育經驗...等)
class MyResume(TemplateView):
    template_name = 'resume_home/my_resume_home.html'

# 建立個人信息的CRUD

#個人信息 R
class ProfileListView(ListView):
    model = Profile
    template_name = 'resume_home/my_information/view_information.html'
    paginate_by = 1  # 每頁顯示1條記錄

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 獲取所有個人資料
        profiles = Profile.objects.all()
        paginator = Paginator(profiles, self.paginate_by)  # 使用分頁器將查詢結果分頁
        page_number = self.request.GET.get('page')  # 獲取當前頁碼
        page_obj = paginator.get_page(page_number)  # 獲取當前頁的對象
        context['profiles'] = page_obj  # 將分頁對象添加到上下文中
        return context

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'resume_home/my_information/create_information.html'
    success_url = reverse_lazy('resume:ProfileShow')

    def form_valid(self, form):
        # 在這裡保存表單數據到資料庫
        self.object = form.save()
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'resume_home/my_information/update_information.html'
    success_url = reverse_lazy('resume:ResumeArea')

    def form_valid(self, form):
        # 將更改應用到資料庫
        self.object = form.save()
        return super().form_valid(form)
    
class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('resume:ResumeArea')

