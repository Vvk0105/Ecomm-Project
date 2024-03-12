from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from  django.contrib import messages
# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #user account creation

            user=User.objects.create(
                username=username,
                password=password,
                email=email
            )
            #create customer account

            Customer.objects.create(
                user=user,
                phone=phone,
                addres=addres
            )
            return redirect('home')
        except Exception as e:
            error_message="Duplication or invalid user"
            messages.error(request,error_message)

    return render(request,'account.html')