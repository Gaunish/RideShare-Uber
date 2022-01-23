from django import forms
class Login(forms.Form):
    user = 'U'
    driver = 'D'
    USER_CHOICES = [(user, 'User'), (driver, 'Driver')]
    user_name = forms.CharField(label='name', max_length = 200)
    email = forms.EmailField(label = 'email', max_length = 250)
    password = forms.CharField(max_length = 200)
    user_type = forms.ChoiceField(choices=USER_CHOICES)
    
