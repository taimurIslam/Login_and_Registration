from django import forms
from .models import Role

class Registration_Form(forms.Form):

    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput
        (
            attrs= {
                    'type':'text',
                    'placeholder':"First Name",
                    'class':'span8',
                    'title':'First Name'
                    }
        ))
    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'placeholder': "Last Name",
                   'class':'span8',
                   'title': 'Last Name'
                   }
        ))

    phone_number = forms.CharField(
        label='Phone Number',
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'pattern': '^[\+][8][8]\d{11}',
                   'maxlength': '15',
                   'title': 'Start with +88',
                   'placeholder': "Phone Number",
                   'class':'span8',
                   }
        ))
    email_address = forms.CharField(
        label='Email Address',
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'email',
                   'maxlength': '30',
                   'title': 'Minimum 30 character!',
                   'placeholder': "Email Address",
                   'class': 'span8',
                   }
        ))
    user_name = forms.CharField(
        label='User Name',
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'pattern': '[A-Za-z0-9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "User Name",
                   'class': 'span8',
                   }
        ))
    user_password = forms.CharField(
        label='User Password',
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'password',
                   'pattern': '[A-Za-z0-9]{3,11}',
                   'maxlength': '11',
                   'title': 'Minimum 3 character!',
                   'placeholder': "User Password",
                   'class':'span8',
                   }
        ))
    user_address = forms.CharField(
        label='User Address',
        required=True,
        widget=forms.TextInput
            (
            attrs={
                   'type': 'text',
                   'maxlength': '30',
                   'placeholder': "User Address",
                   'class': 'span8',
                   }
        ))
    user_photo = forms.ImageField(
        label='Upload Photo',
        required=True,
    )

    CHOICES = [('1', 'Active',), ('0', 'Inactive',)]
    is_active = forms.ChoiceField(
        label='Is Active',
        choices=CHOICES,
        required=True,
        widget=(forms.RadioSelect)
    )

    ROLE_CHOICES = []
    roles = Role.objects.all()
    print(roles)
    for role in roles:
        ROLE_CHOICES.append((role.pk, role.role_title))
    user_title = forms.ChoiceField(
        label='User Title',
        choices=ROLE_CHOICES,
        widget= forms.Select(
            attrs={
                'class': 'span8',
            }
        )

    )


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