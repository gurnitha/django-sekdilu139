# apps/sekdilu139/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from apps.sekdilu139.models import Category, SubCategory, Rank


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug',]
	list_filter = ['name',]    
	search_fields = ['name',]    
	prepopulated_fields = {'slug': ('name',)}    

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug','category_id']
	list_filter = ['name',]    
	search_fields = ['name',]    
	prepopulated_fields = {'slug': ('name',)}    

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):    
	list_display = ['name', 'slug','category_id']
	list_filter = ['category_id',]    
	search_fields = ['name',]    
	prepopulated_fields = {'slug': ('name',)}    
