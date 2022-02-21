from django.contrib import messages
from django.shortcuts import redirect, render
from accounts.models import User
from django.contrib.auth import authenticate, logout as django_logout, login as auth_login
# Create your views here.


def registraion(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST' and request.FILES['image']:
            method_dict = request.POST.copy()
            name = method_dict.get('name')
            phone = method_dict.get('phone')
            email = method_dict.get('email')
            password1 = method_dict.get('passdord1')
            password2 = method_dict.get('passdord2')
            address = method_dict.get('address')
            image = request.FILES['image']

            email.lower()
            email_exists = User.objects.filter(email=email)

            if not email_exists:
                if password1 == password2:
                    user = User.objects.create_user(first_name=name,phone=phone,email=email,address=address,password= password1,image= image)
                    user.is_active = True
                    user.save()
                    messages.success(request, 'Registration Done! You can login now')
                    return redirect('login')
                else:
                    messages.success(request, 'Password did not Matched!')
            else:
                messages.success(request, 'Email Already Taken!')

    return render(request,'accounts/registration.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            email.lower()
            user = authenticate(request,email=email,password=password)
            if user is not None:
                auth_login(request,user)
                return render('/')
            else:
                messages.error(request,'Invalid Email or Password')

    return render(request, 'accounts/login.html')

def logout(request):
    django_logout(request)
    return redirect('login')
