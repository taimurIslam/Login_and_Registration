from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *

# Create your views here.


def login(request):




    if request.method == 'POST':
        form_values = Login_Form(request.POST)
        user_email = form_values['user_email'].value()
        user_password = form_values['user_password'].value()
        print(user_password)
        try:
            user = User.objects.get(email=user_email)
            if user.password == user_password:

                return redirect('Users:admin_page')

        except User.DoesNotExist:
            #messages.error(request, 'User email does not esist')
            print('he he')
    form = Login_Form()
    return render(request, 'other-login.html', {'form': form})




def registration(request):
    return render(request, 'login_and_reg_page/registration.html')

def admin_page(request):
    return render(request, 'index.html')