from django.shortcuts import render


def index(request):
  if request.method == 'GET':
    return render(request, 'index.html', context={"name": "テスト"})
  elif request.method == 'POST':
    return render(request, 'index.html')
