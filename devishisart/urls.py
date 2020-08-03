"""devishisart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from portfolio.admin import *
from portfolio.views import *

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', home),
    path('aboutme/', about),
    path('series/', series_view),
    path('series/soul-searching/', soulsearching),
    path('series/31-days-of-me/', thirtyonedaysofme),
    path('series/wanderlust/', wanderlust),
    path('series/inner-conscience/', innerconscience),
    path('series/regeneration/', regeneration),
    path('series/the-untold-truth/', theuntoldtruth),
    path('series/the-human-trap/', thehumantrap),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)