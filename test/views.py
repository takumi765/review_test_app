from django.shortcuts import redirect, render
from .models import Test

def index(request):
  if request.method == 'GET':
    return render(request, 'index.html', )
  elif request.method == 'POST':
    question = request.POST['question']
    answer = request.POST['answer']
    Test.objects.create(que=question, ans=answer)
    return redirect('index.html')

def create(request):
  if request.method == 'GET':
    return render(request, 'create.html')
  elif request.method == 'POST':
    question = request.POST['question']
    answer = request.POST['answer']
    Test.objects.create(que=question, ans=answer)
    return render(request, 'create.html')

def exam(request):
  if request.method == 'GET':
    return render(request, 'exam.html')
  elif request.method == 'POST':
    return render(request, 'exam.html')

def history(request):
  if request.method == 'GET':
    tests_list = {}
    tests = Test.objects.all()
    tests_list["tests_list"] = tests
    return render(request, 'history.html', tests_list)
  elif request.method == 'POST':
    return render(request, 'history.html')