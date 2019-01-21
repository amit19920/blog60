# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title =models.CharField(max_length=120)
	slug=models.SlugField()
	body=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	def __str__ (self):
		return self.title
	def snippet(self):
		return self.body[:15]+'...'

class Comment(models.Model):
	comment_text = models.TextField(max_length=300)
	commneted_on = models.DateTimeField(auto_now_add=True)
	blog = models.ForeignKey(Article,on_delete=models.CASCADE)
	def __str__(self):
		return "%s %s %s" %(self.comment_text,self.commneted_on,self.blog)
