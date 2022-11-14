from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  free_text = models.CharField(max_length=500, blank=True)
  # 公開アカウントか非公開アカウントか
  visibility = models.CharField(max_length=20, default='private')

class Test(models.Model):
  ## testの科目
  subject = models.CharField(max_length=255, default='')
  ## testのタイトル・解答
  que = models.CharField(max_length=255)
  ans = models.CharField(max_length=255)
  ## testの出題数
  total = models.IntegerField(default=0)
  ## testの正解回数
  correct = models.IntegerField(default=0)
  ## testの正答率
  percent = models.IntegerField(default=0)
  ## ユーザ
  user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
  # 公開テストか非公開テストか
  visibility = models.CharField(max_length=20, default='public')