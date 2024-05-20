from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from .models import Company
import re
from django.core.exceptions import ValidationError

class CompanyRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CompanyRegisterForm, self).__init__(*args, **kwargs)
        self.initial['user_type'] = 2  # Automatically set user_type for 'company'
    
    def clean(self):
        if not re.match(r'^[\u4e00-\u9fa5]{5,}$', self.company_name):
            raise ValidationError("公司名稱格式不正確")
        if not re.match(r'^\d{8}$', self.tin):
            raise ValidationError("統一編號應為 8 位數字")
        if not self.is_valid_tin_number(self.tin):
            raise ValidationError("無效的統一編號")
        if not re.match(r'^[\u4e00-\u9fa5]{2,}$', self.user_name):
            raise ValidationError("姓名格式不正確")
        if not re.match(r'^(0\d{1,2}-?\d{6,8})$', self.tel):
            raise ValidationError("電話號碼格式不正確")


    def is_valid_tin_number(self, tin):
           index = [1, 2, 1, 2, 1, 2, 4, 1]
           arr_tin = list(map(int, tin))
           multiply_arr = [num * index[i] for i, num in enumerate(arr_tin)]
           
           def handle_digits(num):
               if num >= 10:
                   tens_digit = num // 10
                   single_digit = num % 10
                   return tens_digit + single_digit
               return num
           
           result = sum(handle_digits(num) for num in multiply_arr)
           
           if tin[6] == '7':
               return result % 5 == 0 or (result + 1) % 5 == 0
           return result % 5 == 0    

    def save(self, commit=True):
        user = super(CompanyRegisterForm, self).save(commit=False)
        self.clean()
        user.user_type = 2  # Set user_type for 'company'
        if commit:
            user.save()
        return user

class CompanyUpdateForm(UserChangeForm):
    company_name = forms.CharField(max_length=100)
    tin = forms.CharField(max_length=8)
    user_name = forms.CharField(max_length=100)
    tel = forms.CharField(max_length=11)

    class Meta:
        model = CustomUser
        fields = ['username', 'email','company_name','tin','user_name','tel']
    

    def __init__(self, *args, **kwargs):
        super(CompanyUpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']

        self.fields['username'].label = '帳號'
        self.fields['email'].label = '公司信箱'
        self.fields['company_name'].label = '公司名稱'
        self.fields['tin'].label = '統一編號'
        self.fields['user_name'].label = '聯絡人'
        self.fields['tel'].label = '聯絡電話'

        if 'instance' in kwargs:
            user = kwargs['instance']
            company = getattr(user, 'company', None)
            if company:
                self.fields['company_name'].initial = company.company_name
                self.fields['tin'].initial = company.tin
                self.fields['user_name'].initial = company.user_name
                self.fields['tel'].initial = company.tel


    def save(self, commit=True):
        user = super().save(commit=False)
        if user.user_type == 2:
            company, created = Company.objects.update_or_create(
            custom_user=user, 
            defaults={
                'company_name': self.cleaned_data["company_name"],
                'tin': self.cleaned_data["tin"],
                'user_name': self.cleaned_data["user_name"],
                'tel': self.cleaned_data["tel"]
                }
            )
            if commit:
                company.save()
        if commit:
            user.save()
        return user
    
