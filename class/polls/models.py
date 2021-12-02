from django.db import models
from django.utils import timezone

class Category(models.Model):
	title = models.CharField(max_length = 30,unique = True)
	slug = models.SlugField(unique = True)
	photo = models.ImageField('Photo',upload_to = 'class')
	address = models.CharField(max_length = 50)
	date = models.DateField()
	email = models.EmailField('Email')
	phone = models.CharField('Phone', max_length = 15)
	license = models.BooleanField(default = False)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'



class Cigarette(models.Model):
	thickness = (
			('thin','Thin'),
			('thick','Thick')
		)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	title = models.CharField('title',max_length = 30)
	slug = models.SlugField(unique = True)
	photo = models.ImageField('Picture',upload_to = 'class')
	count = models.PositiveIntegerField('count')
	date = models.DateField('Date')
	nicotine = models.PositiveIntegerField(blank = True, null = True)
	xej = models.PositiveIntegerField(blank = True, null = True)
	price = models.PositiveIntegerField('Price')
	choices = models.CharField(choices = thickness, default = 'Thick',max_length = 6)
	description = models.TextField()

	def __str__(self):
		return self.title



