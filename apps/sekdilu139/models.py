# apps/sekdilu139/models.py

# Import django modules
from django.db import models


# MODEL: Category
class Category(models.Model):
	name = models.CharField(max_length=50, blank=False)
	slug = models.SlugField(max_length=250, unique_for_date='created')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural='Categories'

	# Adding string method 
	def __str__(self):
		return self.name