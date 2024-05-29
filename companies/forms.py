from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from .models import Company
from django.utils.translation import gettext_lazy as _


class CompanyRegisterForm(UserCreationForm):
    
    username = forms.CharField(
        label="用戶名",
        help_text="20字或更少。僅限字母、數字和 @/./+/-/_ 符號。",
        error_messages={
            'unique': "此用戶名已存在。",
        }
    )
    email = forms.EmailField(
        label="電子郵件",
        error_messages={
            'unique': "此電子郵件已存在。",
        }
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(),
        help_text=(
            "您的密碼不能與您的其他個人資料過於相似。<br>"
            "您的密碼必須至少包含 8 個字。<br>"
            "您的密碼不能是常用密碼。<br>"
            "您的密碼不能全為數字。<br>"
        )
    )
    password2 = forms.CharField(
        label="確認密碼",
        widget=forms.PasswordInput(),
        help_text="請再次輸入密碼以確認。",
        error_messages={
            'password_mismatch': _("兩次輸入的密碼不同。")
        }
    )
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CompanyRegisterForm, self).__init__(*args, **kwargs)
        self.initial["user_type"] = 2

    def save(self, commit=True):
        user = super(CompanyRegisterForm, self).save(commit=False)
        user.user_type = 2
        if commit:
            user.save()
        return user
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("兩次輸入的密碼不同。"),
                code='password_mismatch',
            )
        return password2

class CompanyUpdateForm(UserChangeForm):
    company_name = forms.CharField(max_length=100)
    tin = forms.CharField(max_length=8)
    user_name = forms.CharField(max_length=100)
    tel = forms.CharField(max_length=11)
    address = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea)
    type = forms.CharField(max_length=50)
    banner = forms.ImageField(required=False)
    logo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "company_name", "tin", "user_name", "tel", "address", "description", "type", "banner", "logo"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(CompanyUpdateForm, self).__init__(*args, **kwargs)
        del self.fields["password"]
        company = kwargs["instance"]
        instance = kwargs.get('instance')
        user = None
        if isinstance(instance, Company):
            user = instance.custom_user
        else:
            user = kwargs.pop('user', None)  
        if user:
            self.fields["username"].initial = user.username
            self.fields["email"].initial = user.email
        self.fields["username"].label = "帳號"
        self.fields["email"].label = "公司信箱"
        self.fields["company_name"].label = "公司名稱"
        self.fields["tin"].label = "統一編號"
        self.fields["user_name"].label = "聯絡人"
        self.fields["tel"].label = "聯絡電話"
        self.fields["address"].label = "地址"
        self.fields["description"].label = "簡介"
        self.fields["type"].label = "類型"
        self.fields["banner"].label = "橫幅"
        self.fields["logo"].label = "Logo"

        if "instance" in kwargs:
            user = kwargs["instance"]
            company = getattr(user, "company", None)
            if company:
                self.fields["company_name"].initial = company.company_name
                self.fields["tin"].initial = company.tin
                self.fields["user_name"].initial = company.user_name
                self.fields["tel"].initial = company.tel
                self.fields["address"].initial = company.address
                self.fields["description"].initial = company.description
                self.fields["type"].initial = company.type
                self.fields["banner"].initial = company.banner
                self.fields["logo"].initial = company.logo

    def save(self, commit=True):
        user = super().save(commit=False)
        if hasattr(user, 'user_type') and user.user_type == 2:
            company, created = Company.objects.update_or_create(
                custom_user=user,
                defaults={
                    "company_name": self.cleaned_data["company_name"],
                    "tin": self.cleaned_data["tin"],
                    "user_name": self.cleaned_data["user_name"],
                    "tel": self.cleaned_data["tel"],
                    "address": self.cleaned_data["address"],
                    "description": self.cleaned_data["description"],
                    "type": self.cleaned_data["type"],
                    "banner": self.cleaned_data["banner"],
                    "logo": self.cleaned_data["logo"],
                },
            )
            if commit:
                company.save()
        if commit:
            user.save()
        return user
