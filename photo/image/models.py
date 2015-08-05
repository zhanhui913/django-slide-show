from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.
class Image(models.Model):
	path = models.FileField(upload_to = '')
	caption = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	upload_date = models.DateField(default = datetime.now, blank=True)
	is_fav = models.BooleanField(default=False)

	@models.permalink
	def get_absolute_url(self):
		return ('image:imageDetail', [self.pk])

	def get_fav_list(self):
		return Image.objects.all().filter(
			is_fav=True
		)

	def __str__(self):
		return self.caption

