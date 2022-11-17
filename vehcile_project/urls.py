"""vehcile_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home.views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path("get-users",ReadGenericApi.as_view()),
    path("delete-update-user/<id>", DeleteDestroyUser.as_view()),
    path('user/<id>', GetUser.as_view()),
    path("ads", AdsReadOrCreate.as_view()),
    path('ads-up-dt-rt/<id>', AdsDeleteUpdate.as_view()),
    path('cars', CarReadOrPost.as_view()),
    path('carud/<id>', CarUpdateDelete.as_view())



    




]