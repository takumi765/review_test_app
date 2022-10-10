from django.db import models

# Create your models here.
class Test(models.Model):
  ## testのタイトル・解答
  que = models.CharField(max_length=255)
  ans = models.CharField(max_length=255)
  ## testの出題数
  total = models.IntegerField(default=0)
  ## testの正解回数
  correct = models.IntegerField(default=0)