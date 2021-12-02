from django.utils import timezone
from django.db import models

# Create your models here.


class Manufacture(models.Model):
	name = models.CharField() 