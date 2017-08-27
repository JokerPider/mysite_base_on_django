# -*- coding: utf-8 -*-

'''修改模型时的操作分三步：

	1. 在models.py中修改模型
	2. 运行python manage.py makemigrations为改动创建迁移记录
	3. 运行python manage.py migrate，将迁移同步到数据库，落实修改动作。
'''

from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Blog(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	blog = models.CharField(max_length=99999)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.author.name
