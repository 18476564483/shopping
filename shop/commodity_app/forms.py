# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UniqueUsernameRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("该用户名已被使用，请重新输入。")
        return username

class AuthenticationForm(forms.Form):
    
    pass

class CheckoutForm(forms.Form):  
    
    pass