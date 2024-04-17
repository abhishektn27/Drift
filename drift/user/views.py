from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def log_out(request):
    logout(request)
    return redirect('home')


def show_account(request):
    context={}

    if request.POST and 'register' in request.POST:
        context['register'] =True
        try:


            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')

            # create user account
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # creates customer account

            customer=Customer.objects.create(
                user=user,
                phone=phone,

            )
            success_massage="user registered successfully"
            messages.success(request,success_massage)

        except Exception as e:
            error_message="Duplicate username or invalid credentials"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')

    return render(request,'account.html',context)
