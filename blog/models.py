from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


STATUS = ((0, "Draft"), (1, "Published"))
SEASON = ((0, "All"), (1, "Spring"), (2, "Summer"),
          (3, "Autumn"), (4, "Winter"))


class Recipe(models.Model):
    """Recipe Database Model"""
    title = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post')
    status = models.IntegerField(choices=STATUS, default=0)
    image = CloudinaryField('image', default='default')
    image_alt = models.CharField(max_length=140, default='default')
    season = models.IntegerField(choices=SEASON, default=0)
    summary = models.TextField(max_length=240)
    ingredients = QuillField()
    instructions = QuillField()
    tags = TaggableManager()
    published_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name="recipe_like", blank=True)

    class Meta:
        "Organise recipes posts by likes in desc order"
        ordering = ['published_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        "Count number of likes per post"
        return self.likes.count()


class Comment(models.Model):
    "Comments Database Model"
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    published = models.DateField(auto_now_add=True)

    class Meta:
        "order by"
        ordering = ['published']

    def __str__(self):
        return f"Comment {self.content} by {self.user}"


class Bookmark(models.Model):
    "Bookmarks database Model"
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='bookmarks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmark_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        "order by"
        ordering = ['-bookmark_created']

    def __str__(self):
        return f"{self.user} bookmarked {self.recipe}"
