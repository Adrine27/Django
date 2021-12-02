from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import New
def index(request):
	return HttpResponse('Hello World')
def cars(request,carid):
	return HttpResponse(f'<h1> Cars Page </h1><p>{carid}</p>')
def show(request):
	my_date = date.today()
	context = {'date':my_date}
	return render(request,'show.html',context)
def new_show(request):
	res = New.objects.all()
	context = {'news' : res}
	return render(request,'new.html',context)

def new_show1(request):
	res = New.objects.all()[:2]
	context = {'news' : res}
	return render(request,'new.html',context)