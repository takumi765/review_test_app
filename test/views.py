from random import randint, random
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Test

def index(request):
  if request.method == 'GET':
    return render(request, 'index.html')

def create(request):
  if request.method == 'GET':
    return render(request, 'create.html')
  elif request.method == 'POST':
    """ 入力された問題文と解答をdbに登録する """
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    Test.objects.create(que=question, ans=answer)
    return render(request, 'create.html')

def exam(request):
  if request.method == 'GET':
    """ dbに登録されたデータをランダムに取り出す """
    counter = Test.objects.all().count()
    test = Test.objects.get(id=randint(1, counter))
    param={'test': test, 'percent': {}}
    if test.total == 0:
      param["percent"]=0
    else:
      param["percent"]=(test.correct/test.total)*100
    return render(request, 'exam.html', param)
    
  elif request.method == 'POST':
    """ 正解数と出題数を変更する """
    test_id = request.POST.get('test_id')
    test = Test.objects.get(id=test_id)
    if "correct" in request.POST:
      test.correct+=1
      test.total+=1
    elif "uncorrect" in request.POST:
      test.total+=1
    test.save()
    return HttpResponseRedirect(reverse('test:exam'))

def history(request):
  if request.method == 'GET':
    """ dbに登録された全てのテストを出力する """
    tests_list = {}
    tests = Test.objects.all()
    tests_list["tests_list"] = tests
    return render(request, 'history.html', tests_list)

  elif request.method == 'POST':
    """ テストidを取得しデータを格納してupdateに送る """
    test_id = request.POST.get('test_id')
    test = Test.objects.get(id=test_id)
    param = {'test': {}}
    param['test']['id'] = test_id
    param['test']['que'] = test.que
    param['test']['ans'] = test.ans
    param['test']['total'] = test.total
    param['test']['correct'] = test.correct
    return render(request, 'update.html', param)

def update(request):
  if request.method == 'POST':
    """ 問題のidに基づきその内容を変更する """
    test_id=request.POST.get('test_id')
    test = Test.objects.get(id=test_id)

    if "update" in request.POST:
      test_que=request.POST.get('test_que')
      test_ans=request.POST.get('test_ans')
      test.que = test_que
      test.ans = test_ans
      test.save()
    elif "delete" in request.POST:
      test.delete()
    return HttpResponseRedirect(reverse('test:history'))