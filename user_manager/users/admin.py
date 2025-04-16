from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ("email", "first_name", "last_name", "user_type", "created_at")
    list_filter = ("user_type",)
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-created_at",)
