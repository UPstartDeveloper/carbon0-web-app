"""carbon0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from carbon0 import views


urlpatterns = [
    # Admin URLs
    path("admin/", admin.site.urls),
    # Project-wide URLs
    path("", views.get_landing, name="landing_page"),
    # Game-related URLs
    path("carbon-quiz/", include("carbon_quiz.urls")),
    # User-Accounts-related URLs
    path("accounts/", include("accounts.urls")),
    # OAuth Lib-related URLs
    path("oauth/", include("social_django.urls", namespace="social")),
    # API-related URLs
    path("api/", include("api.urls")),
    # Garden-related URLs - used for "Plant Vision"
    path("garden/", include("garden.urls")),
]
