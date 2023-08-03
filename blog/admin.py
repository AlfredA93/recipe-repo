from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    "Recipe Admin fields and filtering"
    list_filter = ('status', 'season', 'published_on')
    list_display = ('title', 'status', 'season', 'published_on')
    search_fields = ['title', 'instructions']
