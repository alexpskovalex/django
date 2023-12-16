from django import forms

class CallbackForm(forms.Form):
    name=forms.CharField(label='Ваше имя',max_length=100)
    phone=forms.CharField(label='Ваш телефон',max_length=20 )