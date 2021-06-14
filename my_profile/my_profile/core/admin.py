from django.contrib import admin
from .models import Profile, Email


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = (
        "name",
    )


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )
