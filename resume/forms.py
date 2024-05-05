from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(choices=Profile.SKILL_CHOICES, widget=forms.CheckboxSelectMultiple)
    technologies_used = forms.MultipleChoiceField(choices=Profile.SKILL_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Profile
        exclude = ['deleted_at']
    
    def clean_skills(self):
        skills = self.cleaned_data.get('skills', [])
        return ', '.join(skills)
    
    def clean_technologies_used(self):
        technologies_used = self.cleaned_data.get('technologies_used', [])
        return ', '.join(technologies_used)
    
