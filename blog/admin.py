# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib import admin
from .models import Article,Comment
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)