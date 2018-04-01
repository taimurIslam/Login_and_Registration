from django.shortcuts import render, HttpResponse, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import ValidationError
#from .templates

# Create your views here.


def login(request):

    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return redirect('Users:user_list')

    else:
        if request.method == 'GET':
            form = Login_Form()
            return render(request, 'Users/login.html', {'form': form, 'browser_title': 'User Login'})


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
                            request.session['photo'] = str(user.photo)
                            role = Role.objects.get(id = user.role_id)
                            request.session['role_title'] = role.role_title
                            return redirect('Users:user_list')
                        else:
                            messages.error(request, 'Your Account is not active. Please contact Admin.' )
                    else:
                        messages.error(request, 'Incorrect Email or Password!')

                except User.DoesNotExist:
                    messages.error(request, 'No user found by the Email or Username Provided')

                return redirect('Users:login')
# LOGOUT
def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
        del request.session['username']
        del request.session['id']
        del request.session['role_title']
        del request.session['photo']
        return redirect('Users:login')
    else:
        return redirect('Users:login')


#Registration Form
def registration(request):
    arg = {}
    arg['form'] = Registration_Form
    if request.method == 'POST':
        form_values = Registration_Form(request.POST, request.FILES)
        if form_values.is_valid():

            form_values.save()
            return redirect('Users:registration')
        else:
            #messages.error(request, 'Incorrect Email or Password!')
            arg['form'] = form_values
            return render(request, 'Users/form.html', arg)
    return render(request, 'Users/form.html', arg)




#@login_required('logged_in', 'Users:login')
def user_list(request):
    arg = {}
    arg['users'] = User.objects.all()
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return render(request, 'Users/user_list.html', arg)

    else:
        return redirect('Users:login')

def user_edit(request, user_id):

    user = User.objects.get(pk=user_id)
    print(user.first_name)
def user_delete(request, user_id):
    pass

