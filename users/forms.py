#Import Dependencies
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	github_username = forms.CharField(required=False)
	linkedin_URL = forms.CharField(required=False)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','github_username','linkedin_URL','password1','password2']