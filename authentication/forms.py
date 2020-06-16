from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    # username = forms.CharField(max_length=100, min_length= 3, widget=(forms.TextInput(attrs={'placeholder':'Enter User Name', 'class':'form-control'})))
    # email =  forms.EmailField(widget=(forms.EmailInput(attrs={'placeholder':'Enter email', 'class':'form-control'})))
    # password =  forms.CharField(max_length=100, min_length= 3, widget=(forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'})))

class LoginForm(forms.Form):
    username =  forms.CharField(widget=(forms.TextInput(attrs={'placeholder':'Enter email', 'class':'form-control'})))
    password =  forms.CharField(widget=(forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'})))