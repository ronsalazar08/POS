from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "is_active"]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.is_staff = self.cleaned_data["is_admin"]
        user.is_superuser = self.cleaned_data["is_admin"]
        if commit:
            user.save()
        return user