from .models import UserInfo
from django.forms import ModelForm

class UserForm(ModelForm):
	'''Create Form for user Registration'''

	class Meta:
		model = UserInfo
		fields = ('name','email','phone')
		#fields = '__all__' #register all