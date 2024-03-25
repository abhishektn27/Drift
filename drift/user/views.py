from django.shortcuts import render


# Create your views here.
def user_form(request):
    return render(request,'account.html')
