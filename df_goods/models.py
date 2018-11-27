#  coding: utf-8
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
#商品分类
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

# 商品
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    #图片位置    服务器部署记得看看
    gpic = models.ImageField(upload_to='df_goods')
    # DecimalField具体数字(max_digits=5,最多保留几位 decimal_places=2小数点)
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    #单位default默认值
    gunit = models.CharField(max_length=20,default='500g')
    #点击量  用于排序
    gclick = models.IntegerField()
    #简介
    gjianjie = models.CharField(max_length=200)
    #库存
    gkucun = models.IntegerField()
    #详细介绍
    gcontent = HTMLField()
    #
    gtype = models.ForeignKey('TypeInfo' ,on_delete=models.CASCADE,)

    def __str__(self):
        return self.gtitle.encode('utf-8')

