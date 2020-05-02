from django.db import models


# Create your models here.

class PassportManager(models.Manager):
    # 添加账户信息
    def add_one_passport(self, username, password):
        passport = self.create(username=username, password=password)
        return passport

    # 查找账户信息 根据用户名和密码查找
    def get_one_passport(self, username, password):
        try:
            passport = self.get(username=username, password=password)
        # 如果找不到则返回用户不存在
        except self.model.DoesNotExist:
            passport = None
        return passport


# 用户表
class User(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")
    phone = models.CharField(max_length=50, default="", verbose_name='手机号')
    nickname = models.CharField(max_length=50, default="", verbose_name='昵称')
    name = models.CharField(max_length=50, default="", verbose_name='真实姓名')
    description = models.TextField(max_length=300, default="", verbose_name='个人描述')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 通行证管理
    objects = PassportManager()

    class Meta:
        db_table = 'user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户 " + self.username


# 医生表
class UserDoc(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 通行证管理
    objects = PassportManager()

    class Meta:
        db_table = 'userdoc'
        verbose_name = "用户医生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户医生 " + self.username
