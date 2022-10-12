from django.shortcuts import redirect, render
from .models import Test

def index(request):
  if request.method == 'GET':
    tests_list = {}
    tests = Test.objects.all()
    tests_list["tests_list"] = tests
    return render(request, 'index.html', tests_list)

  elif request.method == 'POST':
    question = request.POST['question']
    answer = request.POST['answer']
    Test.objects.create(que=question, ans=answer)
    return redirect('test')
