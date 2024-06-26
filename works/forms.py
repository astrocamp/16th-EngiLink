from django import forms
from .models import Work
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class WorkForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        input_formats=["%Y-%m"],
        widget=forms.DateInput(attrs={"type": "month"}),
        required=False,
    )
    end_date = forms.DateTimeField(
        input_formats=["%Y-%m"],
        widget=forms.DateInput(attrs={"type": "month"}),
        required=False,
    )
    field_labels = {
        "company_name": "公司名",
        "position": "職位",
        "start_date": "入職時間",
        "end_date": "離職時間",
        "is_current": "在職中",
    }

    class Meta:
        model = Work
        exclude = ["resume", "deleted_at", "created_at", "posit"]

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        for field_name, label in self.field_labels.items():
            self.fields[field_name].label = label

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise ValidationError(_("入職時間不能晚於離職時間"))

        return cleaned_data