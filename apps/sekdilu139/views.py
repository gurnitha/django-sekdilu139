# apps/sekdilu139/views.py

# Import from django modules
from django.shortcuts import render

# Import from loclas
from apps.sekdilu139.models import Person

# HOME PAGE
def home_page(request):
	persons = Person.objects.all()
	print(persons)
	context = {
		'persons':persons,
	}
	return render(request, 'sekdilu139/index.html', context)


# DETAIL PAGE
def detail_page(request, slug):
	person = Person.objects.get(slug=slug)
	persons = Person.objects.all()
	# print(person)
	context = {
		'person':person,
		'persons':persons
	}
	return render(request, 'sekdilu139/detail.html', context)