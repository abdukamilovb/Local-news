from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Sizning foydalanuvchi modeli

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'is_active', 'is_staff','lavozimi')  
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)
    fieldsets = UserAdmin.fieldsets  # Standart user admin interfeysini saqlash
    