from django.db import models

# Create your models here.
from user.models import User


# 科室
class Department(models.Model):
    department_name = models.CharField(max_length=50, verbose_name="科室")

    class Meta:
        db_table = "department"
        verbose_name = '科室表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.department_name


# 症状
class Symptom(models.Model):
    symptom_name = models.CharField(max_length=30, default="", verbose_name='症状')

    class Meta:
        db_table = "symptom"
        verbose_name = "症状表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str("%s" % self.symptom_name)


# 医生
class Doctor(models.Model):
    department = models.ForeignKey(Department, default=None)
    symptom = models.ForeignKey(Symptom, default=None)
    name = models.CharField(max_length=200, verbose_name="医生姓名")
    skill = models.CharField(max_length=200, verbose_name='专长')
    introduce = models.CharField(max_length=500, verbose_name='简介')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "doctor"
        verbose_name = '医生信息'
        verbose_name_plural = verbose_name


# 咨询问题
class Questions(models.Model):
    user = models.ForeignKey(User)
    doctor = models.ForeignKey(Doctor, default=None)
    content = models.CharField(max_length=500, verbose_name="咨询内容")
    comment = models.CharField(max_length=500, default="", verbose_name="评论内容")
    # 后台管理页面上传图片
    image_url = models.ImageField(upload_to='img', default="", verbose_name='图片路径')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = "questions"
        verbose_name = "咨询问题与回复"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.content)


# 药品信息表
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=20, verbose_name="药品名称")
    medicine_num = models.IntegerField(verbose_name="药品库存数量")

    def __str__(self):
        return self.medicine_name

    class Meta:
        db_table = "medicine"
        verbose_name = '药品信息'
        verbose_name_plural = verbose_name


# 购药记录
class MedicineRecord(models.Model):
    user = models.ForeignKey(User, default=None)
    medicine_name = models.CharField(max_length=20, verbose_name="药品名称")
    medicine_num = models.IntegerField(verbose_name="购药数量")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.medicine_name

    class Meta:
        db_table = "medicine_record"
        verbose_name = '购药记录表'
        verbose_name_plural = verbose_name
