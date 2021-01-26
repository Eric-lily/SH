from django.db import models


# Create your models here.
class User(models.Model):
    user_type_choices = (
        (1,'普通用户'),
        (2,'VIP用户'),
        (3,'SVIP用户')
    )
    #账号
    username=models.CharField(max_length=200 ,blank=True,null=True)
    #密码
    password=models.CharField(max_length=200,blank=True,null=True)

    usertype = models.IntegerField(choices = user_type_choices,null=True)

    objects = models.Manager()
    DoesNotExist = models.Manager()

class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=1)
    objects = models.Manager()
    DoesNotExist = models.Manager()

class Person(models.Model):
    p_name = models.CharField(max_length=32)
    p_age = models.IntegerField(default=1)
    p_sex = models.BooleanField(default=False)
    objects = models.Manager()
    DoesNotExist = models.Manager()

class Student(models.Model):
    s_name = models.CharField(max_length=32)
    s_age = models.IntegerField(default=1)
    objects = models.Manager()
    DoesNotExist = models.Manager()

from django.contrib import admin
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Student)