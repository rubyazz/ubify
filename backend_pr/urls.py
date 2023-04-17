"""
URL configuration for backend_pr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from grappelli import urls as grappelli_urls
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from dash import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ubify API",
        default_version="v1",
        description="Ubify is a music app project built using Django, FastAPI, Celery, Django Rest Framework (DRF), Pillow, django-ckeditor, and grappelli. The project aims to create a personalized music streaming platform similar to Spotify, where users can search for albums and songs, add songs to their playlists, make payments for premium features, and interact with artists.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ersultan.abduvalov@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),
    path("grappelli/", include(grappelli_urls)),
    path("api/", include("dash.urls")),
    path("users/", include("users.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/drf-auth/", include("rest_framework.urls")),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^docs/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from allauth.account.views import SignupView
from users.models import CustomUser  

class MySignupView(SignupView):
    model = CustomUser

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        # Изменяем значение поля 'username' на значение поля 'email'
        form.instance.username = form.cleaned_data['email']
        return super().form_valid(form)

# JWT request
# curl \
#   -X POST \
#   -H "Content-Type: application/json" \
#   -d '{"email": "ersultan.abduvalov@gmail.com", "password": "indesit123456"}' \
#   http://localhost:8000/api/token/


# answer
# {"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MTU2MTkyOCwiaWF0IjoxNjgxNDc1NTI4LCJqdGkiOiJjMjhlZDI4MzBiOTA0NTgxOGE4NjJkNjU5NGMwYzM5ZSIsInVzZXJfaWQiOjJ9.17j8EQK1xeMIUrdhiYJfCazvhXsDQYJjHmGcxDbjk-w","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNDc1ODI4LCJpYXQiOjE2ODE0NzU1MjgsImp0aSI6ImMzZGNhYzhmMGNhNzRhMjA4YTk5MGVjNjU2NWZlMjkyIiwidXNlcl9pZCI6Mn0._JfqIqbUDfrmKeLliegV9YZqY25NQ8b3rZFtFxT4GN0"}


# # Example request with access token in headers for login
# curl -H "Authorization: Bearer <eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNDc1ODI4LCJpYXQiOjE2ODE0NzU1MjgsImp0aSI6ImMzZGNhYzhmMGNhNzRhMjA4YTk5MGVjNjU2NWZlMjkyIiwidXNlcl9pZCI6Mn0._JfqIqbUDfrmKeLliegV9YZqY25NQ8b3rZFtFxT4GN0>" https://localhost:8000/api/login


# test user
# honey@gmail.com
# honey123456
