from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import members
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.hashers import make_password
import re
import socket
import geocoder
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

class loginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html') 
class registerprocessView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username=request.POST.get('username','').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        errors = {
            'email_error': None,
            'password_error': None,
            'confirm_password_error': None
        }

      
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            errors['email_error'] = "Email must be a valid address."
        elif members.objects.filter(email=email).exists():
            errors['email_error'] = "Email already exists."

     
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(password_pattern, password):
            errors['password_error'] = 'Password must be at least 8 characters, including uppercase, lowercase, a number, and a special character.'

     
        if password != confirm_password:
            errors['confirm_password_error'] = 'Passwords do not match.'

   
        if any(errors.values()):
            return render(request, 'register.html', {
                'errors': errors,
                'email': email
            })

     
        hashed_password = make_password(password) 
        new_user = members(email=email, password=hashed_password)
        new_user.save()

        messages.success(request, "Registration successful!")
        return redirect('login') 
class registerprocessView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        errors = {
            'email_error': None,
            'password_error': None,
            'confirm_password_error': None
        }
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            errors['email_error'] = "Email must be a valid address."
        elif members.objects.filter(email=email).exists():
            errors['email_error'] = "Email already exists."
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(password_pattern, password):
            errors['password_error'] = 'Password must be at least 8 characters, including uppercase, lowercase, a number, and a special character.'
        if password != confirm_password:
            errors['confirm_password_error'] = 'Passwords do not match.'
        if any(errors.values()):
            return render(request, 'register.html', {
                'errors': errors,
                'email': email,
                'username': username
            })
        hashed_password = make_password(password)  
        new_user = members(email=email, password=hashed_password, username=username)
        new_user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')
class homeView(LoginRequiredMixin, View):
    login_url = '/login/' 
    def get(self, request):
        task_user = members.objects.get(username=request.user.username)  
        return render(request, 'home.html', {
            'task_user': task_user,
            'punchintime': task_user.punch_in,
            'punchouttime': task_user.punch_out,
            'ipaddress':task_user.IPAddr,
            'locationn':task_user.location,
        })
    def post(self, request):
        task_user = members.objects.get(username=request.user.username)  
        if 'punch_in' in request.POST:
            if task_user.punch_in is None: 
                task_user.punch_in = datetime.datetime.now() 
                print("hjjhhuuhu")
                hostname = socket.gethostname()
                print('kjnkjnkjn')
                task_user.IPAddr = socket.gethostbyname(hostname)
                print(task_user.IPAddr)
                g=geocoder.ip("me")
                task_user.location=g.latlng
                print(task_user.location)
                task_user.save()
            else:
               message = "You are already punched in."

        elif 'punch_out' in request.POST:
            if task_user.punch_in is not None and task_user.punch_out is None:  
                task_user.punch_out = datetime.datetime.now() 
                task_user.save()
            else:
                message = "You need to punch in first before punching out."
        return render(request, 'home.html', {
            'task_user': task_user,
            'punchintime': task_user.punch_in,
            'punchouttime': task_user.punch_out,
            'ipaddress':task_user.IPAddr,
            'locationn':task_user.location,
        })
class ListView(LoginRequiredMixin, View):
    login_url = '/login/'  
    def get(self, request):
        task_users = members.objects.all()


        context = {
            'task_users': task_users
        }
        return render(request, 'list.html', context)    
class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

