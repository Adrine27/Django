from django.utils import timezone
from django.db import models

STATIC_CHOICES = (
	('draft','Draft'),
	('published','Published')
	)

class Category(models.Model):
	title = models.CharField('Name Category',max_length=50)
	slug = models.SlugField(unique = True)


	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title

class New(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE,
		verbose_name='Main Category',related_name='main')
	additional_category = models.ManyToManyField(Category, blank = True,related_name = 'additional',verbose_name = 'Additional Categories')
	title = models.CharField('Title',max_length = 150)
	slug = models.SlugField(unique = True)
	content = models.TextField('News Content')
	status = models.CharField('Status',choices = STATIC_CHOICES,
		default = 'published',max_length = 10)
	author = models.CharField('Auther',default='MyNews',max_length=30)
	date = models.DateTimeField('Date',default=timezone.now)
	picture = models.ImageField('Picture',upload_to = 'news')




	def __str__(self):
		return self.title

class User(models.Model):
	Age = (
		('male','Male'),
		('female','Female')
		)
	first_name = models.CharField('First Name',max_length = 20)
	last_name = models.CharField('Last Name',max_length = 30)
	birthday_year = models.DateTimeField('Date',default=timezone.now)
	age = models.PositiveIntegerField('Age')
	gender = models.CharField('Gender',max_length = 10,choices = Age)
	image = models.ImageField('Picture',upload_to = 'user',null = True, blank = True)


def __str__(self):
	return self.first_name
	return self.last_name

