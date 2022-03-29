"""hfo URL Configuration

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
from django.urls import path
from mainapp.views import LandingPage, Login, Register, AddDonation, LogoutView, get_org_by_type

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name="help-for-organizations"),
    path('login/', Login.as_view(), name="log-in"),
    path('register/', Register.as_view(), name="register"),
    path('adddonation/', AddDonation.as_view(), name="add-donation"),
    path('logout/', LogoutView.as_view(), name="log-out"),
    path('get_org_by_type/', get_org_by_type, name='get_org_by_type'),
]


# dodaj odpowiednie ścieżki do widoków.
