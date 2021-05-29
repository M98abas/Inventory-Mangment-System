from django import forms
from .models import LogIn

class Loginform(forms.Form):
	user_name = forms.CharField(widget=forms.TextInput)
	password  = forms.CharField(widget=forms.PasswordInput)


class loginmodel(forms.ModelForm):
	user_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'user_name','id':'user_name','type':'text' ,'name':'username' ,'placeholder':'Username'}))
	password  = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'Password','id':'password','type':'password' ,'name':'password' ,'placeholder':'password'}))

	class Meta:
		model  = LogIn
		fields = ['user_name','password']
