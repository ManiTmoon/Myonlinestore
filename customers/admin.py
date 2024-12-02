from django.contrib import admin
from .models import CustomUser, Address
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'loyalty_points']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address)
