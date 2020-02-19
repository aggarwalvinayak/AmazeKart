from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phoneno = forms.RegexField(regex=r'^\+?1?\d{9,15}$',required=True)
    firstname = forms.CharField(max_length = 50,required = True)
    lastname = forms.CharField(max_length = 50,required = True)

    class Meta:
        model = User
        fields = ("username","firstname","lastname","email", "phoneno","password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phoneno = self.cleaned_data["phoneno"]
        user.firstname = self.cleaned_data["firstname"]
        user.lastname = self.cleaned_data["lastname"]
        if commit:
            user.save()
        return user