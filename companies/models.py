from django.db import models
from django.core.exceptions import ValidationError
from users.models import CustomUser
import re

class Company(models.Model):
    company_name = models.CharField(max_length=100,default='')
    tin = models.CharField(max_length=8,default='')
    user_name = models.CharField(max_length=100,default='')
    tel = models.CharField(max_length=11,default='')
    custom_user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    card_banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    card_logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    card_description = models.TextField(default='')
    card_area = models.CharField(max_length=50, default='')
    card_type = models.CharField(max_length=50, default='')
    tags = models.CharField(max_length=255, default='')

    # def clean(self):
    #     if not re.match(r'^[\u4e00-\u9fa5]{5,}$', self.company_name):
    #         raise ValidationError("公司名稱格式不正確")
    #     if not re.match(r'^\d{8}$', self.tin):
    #         raise ValidationError("統一編號應為 8 位數字")
    #     if not self.is_valid_tin_number(self.tin):
    #         raise ValidationError("無效的統一編號")
    #     if not re.match(r'^[\u4e00-\u9fa5]{2,}$', self.user_name):
    #         raise ValidationError("姓名格式不正確")
    #     if not re.match(r'^(0\d{1,2}-?\d{6,8})$', self.tel):
    #         raise ValidationError("電話號碼格式不正確")


    # def is_valid_tin_number(self, tin):
    #        index = [1, 2, 1, 2, 1, 2, 4, 1]
    #        arr_tin = list(map(int, tin))
    #        multiply_arr = [num * index[i] for i, num in enumerate(arr_tin)]
           
    #        def handle_digits(num):
    #            if num >= 10:
    #                tens_digit = num // 10
    #                single_digit = num % 10
    #                return tens_digit + single_digit
    #            return num
           
    #        result = sum(handle_digits(num) for num in multiply_arr)
           
    #        if tin[6] == '7':
    #            return result % 5 == 0 or (result + 1) % 5 == 0
    #        return result % 5 == 0    

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name