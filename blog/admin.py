# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.contrib import admin

# third party imports

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass