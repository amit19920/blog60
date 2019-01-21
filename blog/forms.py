from django import forms
from .import models

class Comm_ent(forms.ModelForm):
	class Meta:
		model=models.Comment
		fields=['comment_text','blog']

class Bblog(forms.ModelForm):
	class Meta:
		model=models.Article
		fields=['title','slug','body']