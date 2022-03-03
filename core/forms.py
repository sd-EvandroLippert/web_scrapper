
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from core.models import CustomUsuario

class CustomUsuarioCreateForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("As senhas não são iguais"),
    }
    password1 = forms.CharField(
        label=("Senha"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Confirmação da Senha"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )
    class Meta:
        model = CustomUsuario
        labels = {'username': 'Username'}
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user