import re
from django import forms
from django.core.exceptions import ValidationError

def check_name_length(value):
    name_length = len(value)
    if name_length < 4 or name_length >50:
        raise ValidationError('ユーザ名: 4~50文字で入力してください')

def check_password_length(value):
    pass_length = len(value)
    if pass_length < 8 or pass_length > 50:
        raise ValidationError('パスワード: 8~50文字で入力してください')
    
def check_password_re(value):
    if not re.compile(r'^[a-zA-Z0-9]+$').search(value):
        raise ValidationError('パスワード: 半角英数字で入力してください')
    
class UserForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4 or len(name) > 50:
            print ('clean_name')
            raise ValidationError('ユーザ名: 4~8文字で入力してください')
        return name
    
    def clean_password(self):
        password = self.cleaned_data['password']
        error_msg = []
        if len(password) < 8 or len(password) > 50:
            print('パスワード長さだめ')
            error_msg.append(ValidationError('パスワード: 8~50文字で入力してください'))
        if not re.search(r'^[a-zA-z0-9]+$', password):
            print('パスワード文字だめ')
            error_msg.append(ValidationError('パスワード: 半角英数字で入力してください'))
        if error_msg:
            raise ValidationError(error_msg)
        return password