from pyexpat import model
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



class UserRegistrationForm(UserCreationForm):
  email=forms.EmailField(help_text='A valid email',required=True)
  captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
  class Meta:
    model=get_user_model()
    fields =['first_name','last_name','username','email','password1','password2']

  def save(self, commit=True):
    user = super(UserRegistrationForm, self).save(commit=False)
    user.email=self.cleaned_data['email']
    if commit:
      user.save()
      
    return user
  
