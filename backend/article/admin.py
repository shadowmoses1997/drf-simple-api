from django.contrib import admin
from .models import Article





class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author',)
	list_filter = ('created', 'author')
	search_fields = ('title', 'description')
	ordering = ['-created']
 
 
admin.site.register(Article, ArticleAdmin)