from .views import index,cars,show,new_show,new_show1
from django.urls import path
urlpatterns = [
	path('test',index),
	path('car/<int:carid>/',cars),
	path('show/',show),
	path('new/',new_show),
	path('new1/',new_show1),
	]
