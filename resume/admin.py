from django.contrib import admin
from .models import User,Profile
from .forms import ProfileForm


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    exclude = ['deleted_at']
    radio_fields = {'gender': admin.HORIZONTAL, 'experience': admin.HORIZONTAL}


# Register your models here.
admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
