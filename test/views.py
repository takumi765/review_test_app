from random import randint, random
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Test
from .forms import TestForm, UserForm

def login_view(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  if request.method == 'POST':
    name = request.POST.get('name')
    password = request.POST.get('password')
    user = authenticate(username=name, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('test:index'), {'user': user})  
    messages.error(request, '入力情報に間違いがあります')
    return HttpResponseRedirect('.')

def create_user(request):
  if request.method == 'GET':
    return render(request, 'create_user.html')
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      User.objects.create_user(username=request.POST.get('name'), password=request.POST.get('password'))
      return HttpResponseRedirect(reverse('test:login'))
    print(form.errors)
    return render(request, 'create_user.html', {'form': form})
  
def logout_account(request):
  logout(request)
  return HttpResponseRedirect(reverse('test:index'))

def index(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      param = {'date': timezone.now, 'time': timezone.timedelta}
      return render(request, 'index.html', param)
    return HttpResponseRedirect(reverse('test:login'))
    
def create(request):
  if request.method == 'GET':
    return render(request, 'create.html')
  elif request.method == 'POST':
    form = TestForm(request.POST)
    if form.is_valid():
      """ 入力された問題文と解答をdbに登録する """
      Test.objects.create(que=request.POST.get('question'), ans=request.POST.get('answer'), user=request.user)
      return HttpResponseRedirect(reverse('test:create'))
    print(form.errors)
    return render(request, 'create.html', {'form': form})

def exam(request):
  if request.method == 'GET':
    """ dbに登録されたデータをユーザ毎にフィルタリングしてランダムに取り出す """
    test = Test.objects.filter(user=request.user).order_by('?').first()
    return render(request, 'exam.html', {'test': test})
    
  elif request.method == 'POST':
    """ 正解数と出題数を変更する """
    test_id = request.POST.get('test_id')
    test = Test.objects.get(id=test_id)
    if "correct" in request.POST:
      test.correct+=1
      test.total+=1
    elif "uncorrect" in request.POST:
      test.total+=1

    """ パーセント計算 """
    test.percent=(test.correct/test.total)*100
    test.save()
    return HttpResponseRedirect(reverse('test:exam'))

def history(request):
  if request.method == 'GET':
    """ dbに登録された全てのテストを出力する """
    tests_list = {}
    tests = Test.objects.filter(user=request.user)
    tests_list["tests_list"] = tests
    return render(request, 'history.html', tests_list)
  elif request.method == 'POST':
    """ 問題のidに基づきその内容を変更する """
    test_id=request.POST.get('test_id')
    test = Test.objects.get(id=test_id)

    if "update" in request.POST:
      form = TestForm(request.POST)
      if form.is_valid():
        """ 入力された問題文と解答を上書きする """
        question=request.POST.get('question')
        answer=request.POST.get('answer')
        test.que = question
        test.ans = answer
        test.save()
        return HttpResponseRedirect(reverse('test:history'))
      print(form.errors)
      return HttpResponseRedirect(reverse('test:history'))
    elif "delete" in request.POST:
      test.delete()
    return HttpResponseRedirect(reverse('test:history'))