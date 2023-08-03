from django.contrib import admin
from .models import Recipe, Comment, Bookmark, Ingredients


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    "Recipe Admin fields and filtering"
    list_filter = ('status', 'season', 'published_on')
    list_display = ('title', 'status', 'season', 'published_on')
    search_fields = ['title', 'instructions','tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    "Comment Admin fields and filtering"
    list_filter = ('published')
    list_display = ('name', 'recipe', 'published')
    search_fields = ['recipe', 'content']


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    "Bookmark Admin fields and filtering"
    list_filter = ('status', 'bookmark_created')
    list_display = ('user', 'recipe', 'bookmark_created')
    search_fields = ['user', 'recipe']


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    "Ingredient Admin fields and filtering"
    list_filter = ('recipe')
    list_display = ('recipe', 'ingredient', 'amount')
    search_fields = ['recipe', 'ingredient']
