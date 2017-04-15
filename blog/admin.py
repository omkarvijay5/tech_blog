# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.contrib import admin

# third party imports
from blog.models import Category, Article
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass