from django.db import models

class Flower(models.Model):
	COLOR_CHOICE = (
		('red','Red'),
		('white','White')
		)
	name = models.CharField("Flower's name",max_length = 50,unique = True)
	price = models.PositiveIntegerField(default = 1000)
	description = models.TextField(max_length=3000, blank=True, null=True)
	count = models.PositiveSmallIntegerField(default=1)
	color = models.CharField(choices=COLOR_CHOICE, max_length=5)



	def __str__(self):
		return f"{self.id} : {self.name}"

	class Meta:
		verbose_name = 'Flower'
		verbose_name_plural = 'Flowers'



class Watch(models.Model):
	name = models.CharField(max_length=50,unique=True)
	created_at = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return f"{self.created_at} : {self.name}"

	class Meta:
		verbose_name = 'Watch'
		verbose_name_plural = 'Watches'