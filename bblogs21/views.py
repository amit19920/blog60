from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article,Comment
from django import forms
from blog.forms import Comm_ent,Bblog
def home(request):
	articles=Article.objects.all()
	return render(request,'homepage.html',{'art':articles})
def about(request):
	return render(request,'about.html')
def article_details(request,slug):
	article=Article.objects.get(slug=slug)
	comme=Comment.objects.all()
	if request.method=='POST':
		comm=Comm_ent(request.POST)
		if comm.is_valid():
			comm.save(commit=True)
		return redirect("blog:home")
	else:
		comm=Comm_ent()
	return render(request,'article_Deta.html',{'arti':article,'comment': comm,'comme':comme})
def createblogs(request):
	if request.method=='POST':
		f=Bblog(request.POST)
		if f.is_valid():
			create_blog=f.save()
		return redirect("blog:home")
	else:
		create_blog=Bblog()
	return render(request,'createblog.html',{'creat':create_blog})
