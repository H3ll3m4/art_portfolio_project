from django.db import models

# Create your models here.

# Based on this tuto : https://realpython.com/get-started-with-django-1/
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=255)
    info = models.TextField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True)
    slug = models.SlugField(unique=True, null=True)
    categories = models.ManyToManyField("Category", related_name="artworks")


# class Comment(models.Model):
#     author = models.CharField(max_length=60)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     artwork = models.ForeignKey("Artwork", on_delete=models.CASCADE)
