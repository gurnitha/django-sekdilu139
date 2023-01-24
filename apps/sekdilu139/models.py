# apps/sekdilu139/models.py

# Import django modules
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# MODEL: Category
class Category(models.Model):
	name = models.CharField(max_length=50, blank=False)
	slug = models.SlugField(max_length=250)
	# slug = models.SlugField(max_length=250, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural='1. Categories'

	# Adding string method 
	def __str__(self):
		return self.name


# MODEL: Sub-Category
class SubCategory(models.Model):
	name = models.CharField(max_length=50, blank=False)
	slug = models.SlugField(max_length=250)
	# slug = models.SlugField(max_length=250, unique=True)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural='2. Sub categories'

	# Adding string method 
	def __str__(self):
		return self.name


# MODEL: Sosmed
class Sosmed(models.Model):
	name = models.CharField(max_length=50, null=True)
	url = models.URLField(max_length=255, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# Adding string method 
	def __str__(self):
		return self.name

# MODEL: Rank
class Rank(models.Model):
	name = models.CharField(max_length=50, blank=False)
	slug = models.SlugField(max_length=250)
	# slug = models.SlugField(max_length=250, unique=True)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rank')
	# sub_category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_rank')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural='3. Ranks'

	# Adding string method 
	def __str__(self):
		return self.name


# MODEL: Person
class Person(models.Model):

	class Status(models.TextChoices):        
		DRAFT = 'DF', 'Draft'        
		PUBLISHED = 'PB', 'Published'

	name = models.CharField(max_length=50, blank=False)
	slug = models.SlugField(max_length=250, unique=True, help_text='This field will be automatically added.')
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='person')
	image = models.ImageField(upload_to='media/person/', null=True)
	jabatan = models.ForeignKey(Rank, on_delete=models.CASCADE)
	phone = models.CharField(max_length=50, blank=True)
	email = models.CharField(max_length=50, blank=False)
	about_me = RichTextUploadingField(blank=True)
	pendidikan = RichTextUploadingField(blank=True)
	pengalaman_kerja = RichTextUploadingField(blank=True)
	keahlian = RichTextUploadingField(blank=True)
	keluarga = RichTextUploadingField(blank=True)
	filosofi = RichTextUploadingField(blank=True)
	sosmed_id = models.ManyToManyField(Sosmed, related_name='sosmed')
	publish = models.DateTimeField(default=timezone.now)    
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# Defining a default sort order
	class Meta: 
		verbose_name_plural='4. Persons'
		ordering = ['-publish']

	# Adding a database index
	class Meta:        
		ordering = ['-publish']        
		indexes = [            
			models.Index(fields=['-publish']),        
		]

	# Adding string method 
	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('blog:post_detail',
	# 					args=[self.publish.year,
	# 						  self.publish.month,
	# 						  self.publish.day,
	# 						  self.slug])
