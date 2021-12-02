from .views import index
from django.urls import path
from .views import CategoryListView
urlpatterns = [
		path('',index),
		path('',CategoryListView.as_view(), name = 'category'),
]