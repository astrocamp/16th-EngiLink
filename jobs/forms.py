from django.forms import ModelForm
from django import forms
from .models import Job
from .models import Job_Resume
from resumes.models import Resume


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ["title", "openings", "experience", "salary", "address", "description","is_published"]
        labels = {
            "title": "職位名稱",
            "openings": "人數需求",
            "experience": "工作經驗",
            "salary": "工作薪資",
            "address": "工作地點",
            "description": "工作內容",
            "is_published":"是否刊登"
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

class JobResumeForm(forms.ModelForm):
    class Meta:
        model = Job_Resume
        fields = ['job', 'resume']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['resume'].queryset = Resume.objects.filter(user=user)
        self.fields['job'].queryset = Job.objects.filter(company__custom_user__user_type=2)