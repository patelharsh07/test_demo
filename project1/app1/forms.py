from django import forms
from .models import UserMaster

class LoginForms(forms.ModelForm):

	class Meta:
		model=UserMaster
		fields=['UserEmail','UserPassword']

class RegisterForms(forms.ModelForm):

	class Meta:
		model=UserMaster
		fields=['UserName','UserPassword','UserMobile','UserEmail']