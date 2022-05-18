from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter.tix import Form
from django import forms


class LoginForm(forms.Form):
    username= forms.CharField(label="Kullanıcı Adı")
    password= forms.CharField(label="Parola", widget= forms.PasswordInput)

class ResgisterForm (forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)
    
def clean (self):
    username= self.cleaned_data.get("username")
    password= self.cleaned_data.get("password")
    confirm= self.cleaned_data.get("confirm")
    
    if password and confirm and password != confirm:
        raise forms.ValidationError("Parolalar Eşleşmiyor")
    Values ={"username" : username,
             "password" : password}
    
    return Values