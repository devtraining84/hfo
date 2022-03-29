from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm, LoginForm
from .models import Institution, Category


# Create your views here.

class LandingPage(View):
    def get(self, request):
        fundation = Institution.objects.filter(type__contains="fundacja")
        non_governmental_org = Institution.objects.filter(type__contains="organizacja")
        local_money = Institution.objects.filter(type__contains="lokalna")
        ctx = {
            'fundation': fundation,
            'ngo': non_governmental_org,
            'local': local_money
        }
        return render(request, 'index.html', ctx)

class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        category = Category.objects.all()
        ctx = {
            'category': category,
        }
        return render(request, 'form.html', ctx)

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('../register/#register-page')

        else:
            text = 'Nie udało się zalogować'
            return render(request,
                        "login.html",
                        {'form': form, 'text': text})


class Register(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = User.objects.create_user(**form.cleaned_data, email=form.cleaned_data['username'])
            return redirect('../login/#login-page')
        else:
            return render(request, 'register.html', {'form': form, 'error': 'error'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

def get_org_by_type(request):
    type = request.GET.get('type')
    if type is not None:
        org = Institution.objects.filter(type__contains=type)
    else:
        org = Institution.objects.filter(type__contains="funda")
    return render(request, "organization.html", {'org': org})
