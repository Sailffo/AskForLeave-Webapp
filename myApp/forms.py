from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User

class Stu_edit_form(UserChangeForm):
    name = forms.CharField(required=False,max_length=50)

    class Meta:
        model = User
        fields = ("email","username","name",'password')
