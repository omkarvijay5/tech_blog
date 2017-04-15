# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name
