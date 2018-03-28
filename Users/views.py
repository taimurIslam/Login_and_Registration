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
# LOGOUT
def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
        del request.session['username']
        del request.session['id']
        del request.session['role_title']
        return redirect('Users:login')
    else:
        return redirect('Users:login')
#Registration Form
def registration(request):
    form = Registration_Form()
    if request.method == 'POST':
        print('rrrrrrrr')
        form_values = Registration_Form(request.POST or None, request.FILES)
        if form_values.is_valid:
            print('yyyyy')
            new_user = User()
            print('ggggggg')

            # new_user.first_name = form_values['first_name'].value()
            # new_user.last_name = form_values['last_name'].value()
            # new_user.phone = form_values['phone_number'].value()
            # new_user.email = form_values['email_address'].value()
            # new_user.username = form_values['user_name'].value()
            # new_user.password = form_values['user_password'].value()
            # new_user.address = form_values['user_address'].value()
            # new_user.photo = form_values.cleaned_data['user_photo']
            # new_user.is_active = form_values['is_active'].value()
            # new_user.role = form_values['is_active'].value()
            new_user.save()
            return redirect('Users:registration')

    return render(request, 'Users/form.html', {'form': form,'username':request.session['username']})


#@login_required('logged_in', 'Users:login')
def admin_page(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return render(request, 'Users/index.html', {'username':request.session['username']})

    else:
        return redirect('Users:login')

