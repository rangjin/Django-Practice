from django import forms
from django.contrib.auth.hashers import make_password, check_password
from .models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일',
    )

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호',
    )

    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 다시 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호',
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 다릅니다.')
                self.add_error('re_password', '비밀번호가 다릅니다.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일',
    )

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호',
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.add_error('email', '아이디가 없습니다.')
            return

        if not check_password(password, user.password):
            self.add_error('password', '비밀번호가 일치하지 않습니다.')
