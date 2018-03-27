from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q
#from .templates

# Create your views here.


def login(request):

    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return redirect('Users:admin_page')
    else:
        if request.method == 'GET':
            form = Login_Form()
            return render(request, 'other-login.html', {'form': form})


        elif request.method == 'POST':
            form_values = Login_Form(request.POST or None)
            if form_values.is_valid:
                user_username_or_email = form_values['user_username_or_email'].value()
                user_password = form_values['user_password'].value()

                try:
                    user = User.objects.get(Q(email=user_username_or_email)| Q(username= user_username_or_email), password = user_password)
                    if user.password == user_password:
                        if user.is_active is True:
                            request.session['logged_in'] = True
                            request.session['username'] = user.username
                            request.session['id'] = user.pk
                            role = Role.objects.get(id = user.role_id)
                            request.session['role_title'] = role.role_title
                            return redirect('Users:admin_page')
                        else:
                            messages.error(request, 'Your Account is not active. Please contact Admin.' )
                    else:
                        messages.error(request, 'Incorrect Email or Password!')

                except User.DoesNotExist:
                    messages.error(request, 'No user found by the Email or Username Provided')

                return redirect('Users:login')

def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
        del request.session['username']
        del request.session['id']
        del request.session['role_title']
        return redirect('Users:login')
    else:
        return redirect('Users:login')

def registration(request):
    return render(request, 'form.html')


#@login_required('logged_in', 'Users:login')
def admin_page(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return render(request, 'index.html')

    else:
        return redirect('Users:login')

