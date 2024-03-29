from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        },
        max_length=64, label='상품명'
    )

    price = forms.IntegerField(
        error_messages={
            'required': '상품가격을 입력해주세요.'
        }, label='상품가격'
    )

    description = forms.CharField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명'
    )

    stock = forms.IntegerField(
        error_messages={
            'required': '재고를 입력해주세요.'
        }, label='재고'
    )
