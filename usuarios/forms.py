from django import forms
from allauth.account.forms import SignupForm
class MyCustomSignupForm(SignupForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1 and len(password1) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return password1

    def clean_password2(self): #O própio allauth já tem um método clean, e quando eu coloco clean_password2 ele vai sobrescrever o método clean
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
            
        return password2