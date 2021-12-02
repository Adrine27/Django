from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Cigarette

class CategoryListView(ListView):
	template_name = 'category.html'
	queryset = Category.objects.all()
	context_object_name = 'Category'


class CategoryDetailView(DetailView):
	model = Category
	template_name = 'category_detail.html'
	context_object_name = 'Category'

class CigaretteListView(ListView):
	template_name = 'cigarette.html'
	queryset = Cigarette.objects.all()
	context_object_name = 'Cigarette'

class CigaretteDetailView(DetailView):
	model = Cigarette
	template_name = 'cigarette_detail.html'
	context_object_name = 'Cigarette'
