from django.urls import path
from .views import home, user_check_form
urlpatterns = [
		path('',home,name = 'home'),
		path('register',user_check_form, name = 'register')
]