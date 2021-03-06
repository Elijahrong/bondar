"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from ninja import NinjaAPI

from point.api import api_point  # 포인트 url
from userprofile.apis.v1.profile_router import router as file_router

from core import views

api = NinjaAPI()
api.add_router("/images/", file_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
    path("user-edit/", include("userprofile.urls")),
    path("point/", include("point.urls")),
    path("api/point/", api_point.urls),  # 포인트 url
    path("chat/", include("chat.urls")),
    path("welcome/", include("user.urls")),
    path("", include("user.urls")),
    path("", include("like.urls")),
    path("", include("recommend.urls")),
]
