from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Lesson

class LessonListView(ListView):
	template_name = 'lesson.html'
	queryset = Lesson.objects.all()
	context_object_name = 'Lesson'


class LessonDetailView(DetailView):
	model = Lesson
	template_name = 'Lesson_detail.html'
	context_object_name = 'Lesson'