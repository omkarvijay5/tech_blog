# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# python imports
from datetime import datetime

from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey('settings.AUTH_USER_MODEL')
	pub_date = models.DateTimeField(default=datetime.now, help_text='Publication date')
	category = models.ForeignKey('blog.Category')
	hero_image = models.ImageField(upload_to='blog_images/')
	optional_image = models.ImageField(null=True, blank=True)
	text = models.TextField()

