from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import CommonModel


class User(AbstractUser):
    """ 用户模型 """
    avatar = models.ImageField('用户头像', upload_to='avatar/%Y%m', null=True, blank=True)
    nickname = models.CharField('昵称', max_length=32, unique=True)

    class Meta:
        db_table = 'account_user'
