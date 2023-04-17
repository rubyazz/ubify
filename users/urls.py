from django.urls import path

from .views import CustomUserRegistrationView

urlpatterns = [
    path("api/register/", CustomUserRegistrationView.as_view(), name="register"),
]
