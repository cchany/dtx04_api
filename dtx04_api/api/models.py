import datetime
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(help_text="User ID", primary_key=True)
    login_id = models.CharField(max_length=32, unique=True, verbose_name='user 아이디')
    login_pw = models.CharField(max_length=128, verbose_name='user 비밀번호')
    
    def __str__(self):
        return f'[{self.pk}] {self.pk}' 

    def get_absolute_url(self):
        return f'/dtx04/{self.pk}/'
    
    
    
    
    
class User_consultant(models.Model):
    id = models.BigAutoField(help_text="User ID", primary_key=True)
    login_id = models.CharField(max_length=32, unique=True, verbose_name='상담사 아이디')
    login_pw = models.CharField(max_length=128, verbose_name='상담사 비밀번호')
    name = models.CharField(max_length=128, verbose_name='이름')
    inst = models.CharField(max_length=128, verbose_name='소속기관')
    phone = models.CharField(max_length=128, verbose_name='휴대폰')
    email = models.CharField(max_length=128, verbose_name='이메일')
    ckd1 = models.CharField(max_length=128, verbose_name='약관1')
    ckd2 = models.CharField(max_length=128, verbose_name='약관2')
    ckd3 = models.CharField(max_length=128, verbose_name='약관3')
    ckd4 = models.CharField(max_length=128, verbose_name='약관4')
    ckd5 = models.CharField(max_length=128, verbose_name='약관5')


    def get_absolute_url(self):
        return f'/dtx04/{self.pk}/'
    
    def __str__(self):
        return self.login_id
    
    

class User_Medical(models.Model):
    id = models.BigAutoField(help_text="User ID", primary_key=True)
    login_id = models.CharField(max_length=32, unique=True, verbose_name='의료진 아이디')
    login_pw = models.CharField(max_length=128, verbose_name='의료진 비밀번호')


    def get_absolute_url(self):
        return f'/dtx04/{self.pk}/'
    
    def __str__(self):
        return self.login_id
    
 