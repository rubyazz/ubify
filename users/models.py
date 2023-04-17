from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    Permission,
    PermissionsMixin,
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from dash.models import Singer


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    img = models.ImageField(upload_to="profile_images/")
    nickname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    singer = models.OneToOneField(
        Singer, null=True, blank=True, on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_singer = models.BooleanField(default=False)
    is_listener = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "nickname"]

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="customuser_set",  # Add related_name argument to avoid clash
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="customuser_set",  # Add related_name argument to avoid clash
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.nickname

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


# in above we have model likes it must be in each user have their own liked songs how to realize it in models
