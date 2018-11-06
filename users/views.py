import datetime
from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(AuthenticationForm, View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('users:home'))
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and password is not None:
            login(request, user)
            user.last_login = datetime.datetime.now()
            user.save(update_fields=['last_login'])
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect(reverse_lazy('users:home'))
        else:
            messages.warning(request, 'Username or password is incorrect. Or maybe account is inactive')
        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Your account has been logout successfully.')
        return redirect(reverse_lazy('users:login'))


class HomeView(LoginRequiredMixin, View):
    template_name = 'index.html'
    login_url = 'users:login'

    def get(self, request):
        return render(request, self.template_name)
