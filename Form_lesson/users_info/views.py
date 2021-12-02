from django.shortcuts import render, redirect
from .forms import UserForm

def home(request):
	return render(request,'home.html')

def user_check_form(request):
	error = ''

	if request.method == 'POST':
		form = UserForm(request.POST)
		email = request.POST.get('email')
		if form.is_valid() and len(email) > 10:
			form.save()
			return redirect('home')
		else:
			if len(email) < 10:
				error = 'wrong email'
			else:
				error = 'your phone number already used please try another'
	form = UserForm()
	context = {}
	context['user_info'] = form
	context['error'] = error
	return render(request,'user_register.html',context)
