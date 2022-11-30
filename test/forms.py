import re
from django import forms
from django.core.exceptions import ValidationError

def check_name_length(value):
    name_length = len(value)
    if name_length < 4 or name_length >50:
        raise ValidationError('ユーザ名: 4~50文字で入力してください')

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

def check_email(value):
    email_length = len(value)
    if email_length < 4 or email_length > 50:
        raise ValidationError('正しいEmailを入力してください')

def check_password_length(value):
    pass_length = len(value)
    if pass_length < 8 or pass_length > 50:
        raise ValidationError('パスワード: 8~50文字で入力してください')
    
def check_password_re(value):
    if not re.compile(r'^[a-zA-Z0-9]+$').search(value):
        raise ValidationError('パスワード: 半角英数字で入力してください')

def check_question_length(value):
    question_length = len(value)
    if question_length < 1:
        raise ValidationError('問題文を入力してください')
    
def check_answer_length(value):
    answer_length = len(value)
    if answer_length < 1:
        raise ValidationError('問題文を入力してください')

class UserForm(forms.Form):
    name = forms.CharField(
        label='name',
        required=True,
        max_length=100,
        validators=[check_name_length],
    )
    email = forms.CharField(
        label='email',
        required=True,
        max_length=100,
        validators=[check_email],
    )
    password = forms.CharField(
        label='password',
        required=True,
        max_length=100,
        validators=[check_password_length, check_password_re],
    )
    
class TestForm(forms.Form):
    """ 問題文のバリデーション """
    question = forms.CharField(
        label='question',
        required=True,
        max_length=500,
        widget=forms.Textarea,
        validators=[check_question_length],
    )
    """ 解答のバリデーション """
    answer = forms.CharField(
        label='answer',
        required=True,
        max_length=500,
        widget=forms.Textarea,
        validators=[check_answer_length],
    )