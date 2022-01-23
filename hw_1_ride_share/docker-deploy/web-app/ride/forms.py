from django import forms

user = 'U' 
driver = 'D'
USER_CHOICES = [(user, 'User'), (driver, 'Driver')] 

class Login(forms.Form):
    user_name = forms.CharField(label='name', max_length = 200)
    email = forms.EmailField(label = 'email', max_length = 250)
    password = forms.CharField(max_length = 200)
    user_type = forms.ChoiceField(choices=USER_CHOICES)

class Register(forms.Form):
    user_name = forms.CharField(label='name', max_length = 200)
    email = forms.EmailField(label = 'email', max_length = 250) 
    password = forms.CharField(max_length = 200)
    re_passwd = forms.CharField(max_length = 200)
    user_type = forms.ChoiceField(choices=USER_CHOICES)
