from django import forms
from .models import Role, User
from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class Registration_Form(forms.ModelForm):
    CHOICES = [('1', 'Active',), ('0', 'Inactive',)]
    role = forms.ModelChoiceField(label= 'User Title', empty_label='Select User Role', queryset=Role.objects.all(), widget=forms.Select(attrs={'class': 'span8'}), required=True)
    is_active = forms.ChoiceField(label='Is Active', choices=CHOICES, required=True, widget=forms.RadioSelect)
    class Meta:
        model = User
        exclude = ('activation_code', 'password_reset_code')
        widgets = {
                'first_name'    : forms.TextInput(attrs={'type': 'text','placeholder':"First Name", 'title':'First Name', "class":'span8'}),
                'last_name'     : forms.TextInput(attrs={'type': 'text','placeholder': "Last Name",'title': 'Last Name', "class":'span8'}),
                'phone'         : forms.TextInput(attrs={'type': 'text','placeholder': "Phone Number",'pattern': '^[\+][8][8]\d{11}','title': 'Start with +88', "class":'span8'}),
                'email'         : forms.TextInput(attrs={'type': 'text', 'placeholder': "Enter Your Email ",'title': 'Enter Your Mail Here',"class": 'span8'}),
                'username'      : forms.TextInput(attrs={'type': 'text','required' : 'required', 'placeholder': "User Name",'title': 'User Name', "class":'span8'}),
                'password'      : forms.TextInput(attrs={'type': 'password','required' : 'required', 'placeholder': "User Password",'pattern': '[A-Za-z0-9]{3,11}', 'title': 'Minimum 3 character!',"class":'span8'}),
                'address'       : forms.TextInput(attrs={'type': 'text', 'placeholder': "User Address","class": 'span8'})
                 #'photo'        : forms.ImageField(label='Upload Photo')
                }
class Login_Form(forms.Form):
    user_username_or_email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'id' : "inputEmail",
                'class' : "span12",
                'placeholder': "User Name or Email",
                'autocomplete': 'off'
            }
        ))
    user_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id' : "inputPassword",
                'class': "span12",
                'placeholder': "Password",
                'autocomplete': 'off'
            }
        ))
class PasswordResetForm(forms.Form):
    user_email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': "Enter Your Email",
            }
        ))