from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Define the list of fields to be displayed in the change list view
    list_display = (
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_singer",
        "is_listener",
    )

    # Define the list of fields that can be searched in the admin interface
    search_fields = ("first_name", "last_name", "email")

    # Define the fieldsets to be used in the admin interface
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_singer",
                    "is_listener",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_singer",
                    "is_listener",
                ),
            },
        ),
    )

    # Update the ordering attribute to refer to a valid field in CustomUser model
    ordering = ("email",)  # Replace 'username' with 'email' or any other valid field

    # ... other customizations ...


# Register the CustomUser model with the admin site using the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
