from django import forms
from django.db import models
from ..models import Comment
from django.contrib.auth.forms import AuthenticationForm

# from django.utils.translation import ugettext_lazy as _


class CallbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    phone = forms.CharField(
        label="Ваш телефон",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "phone"}),
    )


class BootstrapAuthForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254, widget=forms.TextInput({"placeholder": "Имя пользователя"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput({"placeholder": "Пароль"})
    )


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "comment_text"}),
    )

    class Meta:
        model = Comment  # используемая модель
        fields = ("text",)  # требуется заполнить только поле text
        labels = {"text": "Комментарий"}  # метка к полю формы text
