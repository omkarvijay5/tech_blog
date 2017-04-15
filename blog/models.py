# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# python imports
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """
    Category represents the type of the article which belongs to.
    ex: Hokey, Django, Programming, Politics
    """

    # name of the category ex: Hokey, Cricket, Django
    name = models.CharField(max_length=100)

    description = models.TextField(null=True, blank=True, help_text='Optional description of the category')

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
    Article represents the blog post
    It is created by the user through admin and belongs to a particular category
    """

    # defines the title of the blog
    title = models.CharField(max_length=255)

    # author represents who has created the article
    author = models.ForeignKey(User)

    pub_date = models.DateTimeField(default=datetime.now, help_text='Publication date')

    # represents the category to which the article belongs to
    category = models.ForeignKey('blog.Category')

    # can be a main logo or image which represents the content
    hero_image = models.ImageField(upload_to='images/')

    # extra optional image if needed
    optional_image = models.ImageField(upload_to='images/', null=True, blank=True)

    # main content of the article
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
