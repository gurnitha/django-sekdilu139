# apps/sekdilu139/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from apps.sekdilu139.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug', 'created']
	list_filter = ['name',]    
	search_fields = ['name',]    
	prepopulated_fields = {'slug': ('name',)}    
