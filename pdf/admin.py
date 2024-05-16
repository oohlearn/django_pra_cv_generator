from django.contrib import admin
from .models import Profile

# Register your models here.




class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "skills")
    list_editable = ("email", "skills")
    
    
admin.site.register(Profile, ProfileAdmin)
