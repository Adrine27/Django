from django.db import models
class Lesson(models.Model):
	name = models.CharField(max_length = 50,unique = True)
	slug = models.SlugField('Url',unique = True)
	description = models.TextField('Short description lesson')
	about = models.TextField('Everything about lesson')
	photo = models.ImageField('Photo lesson', upload_to = 'lesson')
	def __str__(self):
		return self.name