from django.db import models

class UserInfo(models.Model):
	'''User Form'''
	name = models.CharField(max_length = 40)
	email = models.EmailField(max_length = 100)
	phone = models.CharField(unique = True,max_length = 15)

	def __str__(self):
		return self.name
