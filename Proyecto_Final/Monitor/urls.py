"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import (
    Index,
    ApiRest,
    SistemPanel,
    SistemDelete,
    LinuxDownload,
    WindowsDownload,
    PythonDownload,
)


urlpatterns = [
    path('', Index.as_view(), name='monitor'),
    path('api/postData', ApiRest.as_view()),
    path('<int:id>', SistemPanel.as_view()),
    path('<int:id>/delete', SistemDelete.as_view()),
    path('linux/download', LinuxDownload.as_view()),
    path('windows/download', WindowsDownload.as_view()),
    path('python/download', PythonDownload.as_view()),
]