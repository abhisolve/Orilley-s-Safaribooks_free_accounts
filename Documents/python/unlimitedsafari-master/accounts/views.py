from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate



class Signup(View):
    template_name = 'dashboard/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = "" 
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email is not None:
            username = email.split("@")[0]
        if password is not None:
            password = make_password(password)

        try:
            user = User.objects.create(username=username, email=email, password=password)
            user = authenticate(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
        except Exception as e:
            print(e)
            pass


class  Signin(View):
    template_name = 'dashboard/signin.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = email.split("@")[0]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')


class Home(View):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)
