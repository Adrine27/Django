from django.utils import timezone
from django.db import models



STATUS_CHOICES = (
    ('published','Published'),
    ('draft','Draft')
    )

class Manufacture(models.Model):
	name = models.CharField("Manufacture's name",max_length = 50)
	slug = models.SlugField(unique=True)
	photo = models.ImageField('Picture',upload_to = 'car')
	status = models.CharField('status',choices = STATUS_CHOICES,default = 'Published',max_length = 10)
	address = models.CharField('Address',max_length = 250)

	def __str__(self):
		return self.name


class Car(models.Model):
	COLOR_CHOICES = (
	('white','White'),
	('black','Black'),
	('red','Red'),
	('yellow','Yellow'),
	('silver','Silver')
	)

	manufacture = models.ForeignKey(Manufacture,on_delete = models.CASCADE)
	name = models.CharField("Car's name",max_length = 20)
	slug = models.SlugField(unique = True)
	email = models.EmailField('Email')
	phone = models.CharField('Phone number',max_length = 9)
	date = models.DateField('Date')
	status = models.CharField('Status',choices = STATUS_CHOICES,default = 'Published',max_length = 10)
	color = models.CharField('Color', choices = COLOR_CHOICES,max_length = 6)
	photo = models.ImageField('Picture',upload_to = 'car')


	def __str__(self):
		return self.name

