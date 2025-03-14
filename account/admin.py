from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ['id','first_name','last_name','email','city','is_active']
    list_filter = ['is_active','is_superuser','is_staff']
    ordering = ['id','city']
    filter_horizontal = ['groups','user_permissions']
    search_fields = ["first_name","last_name","email"]
    fieldsets = [
        ('User Credentials', {"fields":("email","password")}),
        ('Personal Information', {"fields":("first_name","last_name","city","phone")}),
        ('Permissions', {"fields":("is_active","is_staff","is_superuser")}),
        ('Important Dates', {"fields":("created_at","updated_at","last_login")}),
        ('Groups and Permissions', {"fields":("groups","user_permissions")}),
    ]
    readonly_fields = ['created_at','updated_at']