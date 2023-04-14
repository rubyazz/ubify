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
from django.urls import path, include
from grappelli import urls as grappelli_urls
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("grappelli/", include(grappelli_urls)),
    path("", include("dash.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# request
# curl \
#   -X POST \
#   -H "Content-Type: application/json" \
#   -d '{"email": "ersultan.abduvalov@gmail.com", "password": "indesit123456"}' \
#   http://localhost:8000/api/token/


# answer
# {"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MTU2MTkyOCwiaWF0IjoxNjgxNDc1NTI4LCJqdGkiOiJjMjhlZDI4MzBiOTA0NTgxOGE4NjJkNjU5NGMwYzM5ZSIsInVzZXJfaWQiOjJ9.17j8EQK1xeMIUrdhiYJfCazvhXsDQYJjHmGcxDbjk-w","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNDc1ODI4LCJpYXQiOjE2ODE0NzU1MjgsImp0aSI6ImMzZGNhYzhmMGNhNzRhMjA4YTk5MGVjNjU2NWZlMjkyIiwidXNlcl9pZCI6Mn0._JfqIqbUDfrmKeLliegV9YZqY25NQ8b3rZFtFxT4GN0"}


# # Example request with access token in headers for login
# curl -H "Authorization: Bearer <eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNDc1ODI4LCJpYXQiOjE2ODE0NzU1MjgsImp0aSI6ImMzZGNhYzhmMGNhNzRhMjA4YTk5MGVjNjU2NWZlMjkyIiwidXNlcl9pZCI6Mn0._JfqIqbUDfrmKeLliegV9YZqY25NQ8b3rZFtFxT4GN0>" https://localhost:8000/api/login
